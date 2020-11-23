from django.db import models
from django.core.validators import RegexValidator


class Order(models.Model):
    class ShippingMethod(models.TextChoices):
        PICKUP_1 = 'PICKUP_1'
        PICKUP_2 = 'PICKUP_2'
        FREE_SAME_DAY_DRONE = 'FREE_SAME_DAY_DRONE'
        COST_SAME_DAY_DRONE = 'COST_SAME_DAY_DRONE'
        FREE_TWO_DAY_TRUCK = 'FREE_TWO_DAY_TRUCK'
        COST_SAME_DAY_TRUCK = 'COST_SAME_DAY_TRUCK'
        COST_TWO_DAY_TRUCK = 'COST_TWO_DAY_TRUCK'

    user = models.ForeignKey(
        to='users.CustomUser', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, default='')
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex='\d{5}'
        )
    ])
    phone = models.CharField(max_length=10, validators=[
        RegexValidator(
            regex='\d{10}'
        )
    ])
    shipping_method = models.CharField(
        max_length=128, choices=ShippingMethod.choices)
    weight = models.FloatField()
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(null=True, blank=True)
    driver = models.ForeignKey(
        to='users.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='driver')


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to='products.Product',
                                on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    # Because it changes, we want to save the price on day of purchase
    price = models.DecimalField(max_digits=8, decimal_places=2)
