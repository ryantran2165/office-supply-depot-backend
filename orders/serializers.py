from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'subtotal', 'delivery_cost', 'taxes', 'total', 'delivery_method', 'date_ordered', 'first_name',
                  'last_name', 'phone', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'date_delivered',)


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'address_1',
                  'address_2', 'city', 'state', 'zip_code',)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('item', 'quantity', 'price',)
