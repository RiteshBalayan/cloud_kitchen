from django.contrib import admin
from .models import Kitchen, Dish, Inventory, Order  # Import the models

@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_verified', 'chef']  # Customize the list display as needed
    search_fields = ['chef__name']  # Assume the Chef model has a 'name' field; adjust as necessary

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'chef', 'description', 'price', 'is_verified', 'total_orders']
    search_fields = ['description', 'ingredients', 'recipe', 'chef__name']  # Adjust according to your Chef model
    list_filter = ['is_verified', 'chef']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'kitchen', 'dish', 'ready_at', 'quantity', 'delivery_method', 'delivery_radius']
    list_filter = ['delivery_method', 'kitchen', 'dish']
    search_fields = ['kitchen__name', 'dish__name']  # Adjust according to your Kitchen and Dish model fields

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'inventory', 'is_customer_delivered', 'is_chef_delivered','order_conformed']
    list_filter = ['is_customer_delivered', 'is_chef_delivered', 'order_conformed']
    search_fields = ['customer__name', 'inventory__id']  # Adjust according to your Profile and Inventory model fields

