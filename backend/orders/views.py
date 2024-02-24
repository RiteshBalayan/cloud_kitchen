from rest_framework import generics, permissions
from .models import Inventory
from .serializers import InventorySerializer

class InventoryList(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        This view should return a list of all the inventory
        items where the quantity is more than zero.
        """
        return Inventory.objects.filter(quantity__gt=0)
