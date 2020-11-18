from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'price',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'address_1', 'address_2', 'city',
                  'state', 'zip_code', 'phone', 'shipping_method', 'subtotal', 'tax', 'shipping_cost', 'date_ordered', 'date_delivered', 'items',)

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        # Create OrderItem's
        for item in items:
            OrderItem.objects.create(order=order, **item)

        return order


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'address_1',
                  'address_2', 'city', 'state', 'zip_code', 'phone',)
