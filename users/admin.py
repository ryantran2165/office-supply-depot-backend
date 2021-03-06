from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_active', 'is_driver',)
    list_filter = ('email', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'is_driver')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_driver')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_driver')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email', 'first_name', 'last_name',)


admin.site.register(CustomUser, CustomUserAdmin)
