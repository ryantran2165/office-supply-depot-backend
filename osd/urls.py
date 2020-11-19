"""osd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from products.views import ProductView
from carts.views import CartView
from orders.views import OrderView
from django.contrib.auth.models import Group

router = routers.DefaultRouter()
router.register(r'products', ProductView, 'product')
router.register(r'carts', CartView, 'cart')
router.register(r'orders', OrderView, 'order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('users/', include('users.urls')),
    path('', include(router.urls)),
]

admin.site.unregister(Group)
admin.site.site_header = 'Office Supply Depot Administration'
admin.site.index_title = 'Site administration'
admin.site.site_title = 'OSD Admin'
