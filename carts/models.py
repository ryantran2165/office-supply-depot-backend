from django.db import models


class Cart(models.Model):
    user = models.ForeignKey(
        to='users.CustomUser', on_delete=models.CASCADE)
    product = models.ForeignKey(
        to='products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
