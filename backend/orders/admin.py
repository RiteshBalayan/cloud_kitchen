from django.contrib import admin
from .models import Kitchen, Dish, Inventory, Order  

@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    search_fields = ['chef__name']  

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ['description', 'ingredients', 'recipe', 'chef__name']  
    list_filter = ['is_verified', 'chef']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_filter = ['delivery_method', 'kitchen', 'dish']
    search_fields = ['kitchen__name', 'dish__name']  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['is_customer_delivered', 'is_chef_delivered', 'order_conformed']
    search_fields = ['customer__name', 'inventory__id']  

