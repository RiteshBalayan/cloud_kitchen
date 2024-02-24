from django.urls import path
from .views import InventoryList

urlpatterns = [
    path('inventories/', InventoryList.as_view(), name='inventory-list'),
]