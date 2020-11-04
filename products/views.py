from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .serializers import ProductSerializer
from .models import Product


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        # Retrieve query params
        items = int(self.request.query_params.get('items', 20))
        page = int(self.request.query_params.get('page', 1))
        query = self.request.query_params.get('query', "")
        category = self.request.query_params.get('category', "")
        subcategory = self.request.query_params.get('subcategory', "")

        # Filter by query, category, and subcategory
        products = self.get_queryset()
        if query != "":
            products = products.filter(name__icontains=query)
        if category != "":
            products = products.filter(category=category)
        if subcategory != "":
            products = products.filter(subcategory=subcategory)

        # Calculate queryset based on number of items desired and page
        start = items * (page - 1)
        end = items * page
        queryset = products[start:end]

        # Serialize and return
        serializer = self.get_serializer(queryset, many=True)
        return Response({"products": serializer.data, "count": queryset.count()})

    @action(detail=False)
    def list_similar(self, request):
        # Retreive query params
        items = int(self.request.query_params.get('items', 4))
        product_id = int(self.request.query_params.get('id'))

        # Retrieve target product category and subcategory
        products = self.get_queryset()
        product = products.get(pk=product_id)
        category = product.category
        subcategory = product.subcategory

        # Exclude target product and filter by category and subcategory
        products = products.exclude(pk=product_id)
        if category != "":
            products = products.filter(category=category)
        if subcategory != "":
            products = products.filter(subcategory=subcategory)

        # Rank similarity by target product's name found in other products' names and descriptions
        vector = SearchVector('name', 'description')
        query = SearchQuery(product.name)
        products = products.annotate(
            rank=SearchRank(vector, query)).order_by('-rank')

        # Calculate queryset based on number of items desired
        queryset = products[:items]

        # Serialize and return
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
