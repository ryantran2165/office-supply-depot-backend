from rest_framework import viewsets, mixins
from .serializers import CartSerializer
from .models import Cart


class CartView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Each user has one cart.
    Allow: GET, PUT
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # Return only the authenticated user's cart
    def get_object(self):
        return Cart.objects.get(user_id=self.request.user)
