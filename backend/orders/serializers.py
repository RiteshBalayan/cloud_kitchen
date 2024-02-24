from rest_framework import serializers
from core.models import Profile, Chef, Photo
from .models import Dish, Inventory, Kitchen, Order
from django.contrib.auth.models import User


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name']  # Include other fields if needed

class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ['name']  # Include other fields if needed

class InventorySerializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True)
    kitchen = KitchenSerializer(read_only=True)
    class Meta:
        model = Inventory
        fields = ['kitchen', 'dish', 'ready_at', 'quantity', 'delivery_method', 'delivery_radius']