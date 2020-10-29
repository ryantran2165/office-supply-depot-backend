from django.contrib import admin
from .models import Order
from users.models import CustomUser


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'user', 'driver',)
    list_filter = ('id', 'user', 'driver',)
    search_fields = ('id', 'user', 'driver',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "driver":
            kwargs["queryset"] = CustomUser.objects.filter(is_driver=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Order, OrderAdmin)
