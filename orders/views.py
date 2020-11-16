from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    # Return only the current user's orders
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    # On create, save the user
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
