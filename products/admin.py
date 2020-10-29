from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'inventory',)
    list_filter = ('id', 'name', 'inventory',)
    search_fields = ('id', 'name', 'inventory',)


admin.site.register(Product, ProductAdmin)
