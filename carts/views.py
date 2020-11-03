from rest_framework import viewsets, mixins
from .serializers import CartSerializer
from .models import Cart


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    # Return only the current user's cart
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    # On create, save the user
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
