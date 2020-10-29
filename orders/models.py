from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Order(models.Model):
    class DeliveryMethod(models.TextChoices):
        FREE_SAME_DAY_DRONE = 'FREE_SAME_DAY_DRONE'
        FREE_TWO_DAY_TRUCK = 'FREE_TWO_DAY_TRUCK'
        PREMIUM_SAME_DAY_TRUCK = 'PREMIUM_SAME_DAY_TRUCK'
        PREMIUM_SAME_DAY_DRONE = 'PREMIUM_SAME_DAY_DRONE'
        PREMIUM_TWO_DAY_TRUCK = 'PREMIUM_TWO_DAY_TRUCK'

    user = models.ForeignKey(
        to='users.CustomUser', on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2)
    taxes = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_method = models.CharField(
        max_length=128, choices=DeliveryMethod.choices)
    date_ordered = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = PhoneNumberField()
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex='^\d{5}$'
        )
    ])
    date_delivered = models.DateTimeField(null=True, blank=True)
    driver = models.ForeignKey(
        to='users.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='driver')


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE)
    item = models.ForeignKey(to='products.Product',
                             on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
