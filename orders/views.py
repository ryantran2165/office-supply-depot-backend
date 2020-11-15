from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # On create, save the user
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
