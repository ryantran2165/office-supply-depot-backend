from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import OrderSerializer, DeliverySerializer
from .models import Order
from django.utils import timezone


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    # Return only the current user's orders
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    # On create, save the user
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=False)
    def list_deliveries(self, request):
        queryset = Order.objects.filter(
            driver=request.user, date_delivered=None)
        serializer = DeliverySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def set_delivered(self, request, pk):
        order = Order.objects.get(driver=request.user, id=pk)
        order.date_delivered = timezone.now()
        order.save()
        serializer = DeliverySerializer(order)
        return Response(serializer.data)
