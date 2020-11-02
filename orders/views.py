from rest_framework import viewsets
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class OrderView(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def create_order(self, request, pk=None):
        """ Creates a new order. The order details should be in the post data.
        """
        # TO FINISH
        return Response({'status': 'Order Created')

    @action(detail=True, methods=['post'])
    def get_order_items(self, request, pk=None):
        """ Given an order_id, return all the OrderItems associated with it.
            The expected post data should be of the form: {"order_id":"1"}
        """
        print(request.data['order_id'])
        order_id = request.data['order_id']
        order_items = OrderItem.objects.filter(order_id=order_id)
        if len(order_items) == 0:
            return Response({'order_items': []})
        order_items_serializer = OrderItemSerializer(order_items, many=True)
        return Response({'order_items': order_items_serializer.data})

    def list(self, request):
        """ Lists all the orders of the current user.
        """
        orders = Order.objects.filter(user_id=request.user.id)
        if len(orders) == 0:
            return Response({'orders': ''})
        order_serializer = OrderSerializer(orders, many=True)
        return Response({'orders': order_serializer.data})
