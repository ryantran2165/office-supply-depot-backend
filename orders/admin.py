from django.contrib import admin
from .models import Order
from users.models import CustomUser


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'user', 'shipping_method',
                    'driver', 'date_delivered',)
    list_filter = ('id', 'user', 'shipping_method',
                   'driver', 'date_delivered',)
    search_fields = ('id', 'user__email', 'user__first_name', 'user__last_name', 'shipping_method',
                     'driver__email', 'driver__first_name', 'driver__last_name', 'date_delivered',)
    readonly_fields = ('user', 'first_name', 'last_name', 'city', 'state', 'zip_code', 'phone',
                       'shipping_method', 'weight', 'tax', 'shipping_cost', 'address_1', 'address_2',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'driver':
            kwargs['queryset'] = CustomUser.objects.filter(is_driver=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        driver = form.base_fields['driver']
        driver.widget.can_add_related = False
        driver.widget.can_delete_related = False
        driver.widget.can_change_related = False

        return form

    def has_add_permission(self, request):
        return False


admin.site.register(Order, OrderAdmin)
