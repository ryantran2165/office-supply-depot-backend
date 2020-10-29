from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'user', 'item', 'quantity',)
    list_filter = ('id', 'user', 'item', 'quantity',)
    search_fields = ('id', 'user', 'item', 'quantity',)


admin.site.register(Cart, CartAdmin)
