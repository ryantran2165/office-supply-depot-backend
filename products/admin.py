from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'inventory', 'category', 'subcategory',)
    list_filter = ('id', 'name', 'inventory', 'category', 'subcategory',)
    search_fields = ('id', 'name', 'inventory', 'category', 'subcategory',)


admin.site.register(Product, ProductAdmin)
