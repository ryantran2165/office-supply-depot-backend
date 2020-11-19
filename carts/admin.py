from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'user', 'product', 'quantity',)
    list_filter = ('id', 'user', 'product', 'quantity',)
    search_fields = ('id', 'user__email', 'user__first_name',
                     'user__last_name', 'product__name', 'quantity',)


admin.site.register(Cart, CartAdmin)
