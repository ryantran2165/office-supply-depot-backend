from rest_framework import viewsets, mixins
from .serializers import CartSerializer
from .models import Cart
from django.shortcuts import get_list_or_404


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    # Return only the current user's cart
    def get_queryset(self):
        return get_list_or_404(Cart, user_id=self.request.user)

    # On create, save the user
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
