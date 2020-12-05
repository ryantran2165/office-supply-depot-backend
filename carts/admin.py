from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'user', 'product', 'quantity',)
    list_filter = ('id', 'user', 'product', 'quantity',)
    search_fields = ('id', 'user__email', 'user__first_name',
                     'user__last_name', 'product__name', 'quantity',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        user = form.base_fields['user']
        user.widget.can_add_related = False
        user.widget.can_delete_related = False
        user.widget.can_change_related = False

        product = form.base_fields['product']
        product.widget.can_add_related = False
        product.widget.can_delete_related = False
        product.widget.can_change_related = False

        return form


# admin.site.register(Cart, CartAdmin)
