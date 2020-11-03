from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        items = int(self.request.query_params.get('items', 20))
        page = int(self.request.query_params.get('page', 1))
        query = self.request.query_params.get('query', "")
        category = self.request.query_params.get('category', "")
        subcategory = self.request.query_params.get('subcategory', "")

        products = Product.objects.all()
        if query != "":
            products = products.filter(name__icontains=query)
        if category != "":
            products = products.filter(category=category)
        if subcategory != "":
            products = products.filter(subcategory=subcategory)

        start = items * (page - 1)
        end = items * page
        queryset = products[start:end]

        serializer = ProductSerializer(queryset, many=True)
        return Response({"products": serializer.data, "count": queryset.count()})
