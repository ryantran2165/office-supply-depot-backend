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
        start = items * (page - 1)
        end = items * page
        queryset = Product.objects.all()[start:end]
        serializer = ProductSerializer(queryset, many=True)
        return Response({"products": serializer.data, "count": Product.objects.count()})
