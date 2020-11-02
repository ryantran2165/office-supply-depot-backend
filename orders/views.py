from rest_framework import viewsets
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import CustomUser
from products.models import Product
from datetime import datetime


class OrderView(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def create_order(self, request, pk=None):
        """ Creates a new order. The order details should be in the post data.
        """
        # Example Post Data: {"items": {"1": "2"}, "subtotal": "2", "delivery_cost": "2", "taxes": "2", "total": "6", "delivery_method": "FREE_SAME_DAY_DRONE", "first_name": "here", "last_name": "ded", "phone": "+13648593894", "address_1": "huh","address_2": "", "city": "s", "state": "s", "zip_code": "53789", "date_delivered": "2020-11-03T16:10", "date_ordered": "2020-11-03T16:10"}
        order_data = request.data
        if (order_data['items'] and order_data['subtotal'] and order_data['delivery_cost'] and order_data['taxes']
            and order_data['total'] and order_data['total'] and order_data['delivery_method'] and order_data['first_name']
            and order_data['last_name'] and order_data['phone'] and order_data['address_1'] and order_data['city']
            and order_data['state'] and order_data['zip_code']):
            #print(str(request.user)[3:-1])
            user = CustomUser.objects.filter(email=str(request.user)[3:-1])[0] # Find the right user based on email address, probably a better way to do this
            order = Order(user=user, subtotal=order_data['subtotal'], delivery_cost=order_data['delivery_cost'],
                          taxes=order_data['taxes'], total=order_data['total'], delivery_method=order_data['delivery_method'],
                           date_ordered=datetime.today().strftime('%Y-%m-%dT%H:%M'), first_name=order_data['first_name'], last_name=order_data['last_name'],
                           phone=order_data['phone'], address_1=order_data['address_1'], city=order_data['city'], state=order_data['state'],
                           zip_code=order_data['zip_code'])
            order.save()

            for key in order_data['items']:
                item = Product.objects.filter(id=key)[0]
                order_item = OrderItem(order=order, item=item, quantity=order_data['items'][key], price=item.price)
                order_item.save()

            return Response({'status': 'Order Created'})
        else:
            return Response({'status': 'Error'})

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
