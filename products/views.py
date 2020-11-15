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
        items = int(request.query_params.get('items', 20))
        page = int(request.query_params.get('page', 1))
        query = request.query_params.get('query', '')
        category = request.query_params.get('category', '')
        subcategory = request.query_params.get('subcategory', '')
        min_price = float(request.query_params.get('min_price', 0))
        max_price = float(request.query_params.get(
            'max_price', float('inf')))
        sort = request.query_params.get(
            'sort', 'Best Match' if query != '' else 'Name A to Z')

        # Filter
        products = self.get_queryset()
        if query != '':
            products = products.filter(name__icontains=query)
        if category != '':
            products = products.filter(category=category)
        if subcategory != '':
            products = products.filter(subcategory=subcategory)
        products = products.filter(price__gte=min_price)
        products = products.filter(price__lte=max_price)

        # Sort
        if sort == 'Best Match':
            products = products.annotate(
                rank=SearchRank(SearchVector('name', 'description'), SearchQuery(query))).order_by('-rank')
        elif sort == 'Name A to Z':
            products = products.order_by('name', 'price')
        elif sort == 'Name Z to A':
            products = products.order_by('-name', 'price')
        elif sort == 'Price Low to High':
            products = products.order_by('price', 'name')
        elif sort == 'Price High to Low':
            products = products.order_by('-price', 'name')

        # Calculate queryset based on number of items desired and page
        start = items * (page - 1)
        end = items * page
        queryset = products[start:end]

        # Serialize and return
        serializer = self.get_serializer(queryset, many=True)
        return Response({'products': serializer.data, 'count': products.count()})

    @action(detail=False)
    def list_similar(self, request):
        # Retreive query params
        items = int(request.query_params.get('items', 4))
        product_id = int(request.query_params.get('id'))

        # Retrieve target product category and subcategory
        products = self.get_queryset()
        product = products.get(pk=product_id)
        category = product.category
        subcategory = product.subcategory

        # Exclude target product and filter by category and subcategory
        products = products.exclude(pk=product_id)
        if category != '':
            products = products.filter(category=category)
        if subcategory != '':
            products = products.filter(subcategory=subcategory)

        # Rank similarity by target product's name found in other products' names and descriptions
        products = products.annotate(
            rank=SearchRank(SearchVector('name', 'description'), SearchQuery(product.name))).order_by('-rank')

        # Calculate queryset based on number of items desired
        queryset = products[:items]

        # Serialize and return
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
