from django.db import models
from core.models import Photo, Profile, Chef


class Kitchen(models.Model):
    # Photos of the kitchen
    name = models.TextField(blank=True)
    photos = models.ManyToManyField(Photo, related_name='kitchens', blank=True)
    is_verified = models.BooleanField(default=False)  # Changed to 'is_verified' for clarity
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='kitchens')  # Specify Chef as a string if it's defined elsewhere

class Dish(models.Model):  # Renamed to 'Dish' to follow Django's convention for Model names (singular)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='dishes')
    description = models.TextField()  # Corrected spelling
    ingredients = models.TextField()
    recipe = models.TextField()
    photos = models.ManyToManyField(Photo, related_name='dishes', blank=True)
    is_verified = models.BooleanField(default=False)  # Changed to 'is_verified' for clarity
    price = models.FloatField()
    total_orders = models.IntegerField()

class Inventory(models.Model):
    DELIVERY_CHOICES = [  # Renamed to uppercase to follow Python's constant naming convention
        ('Delivery', 'Delivery'),
        ('Collect', 'Collect'),
    ]

    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='inventory')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='inventory')  # Changed 'Dishes' to 'Dish'
    ready_at = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='Delivery')  # Corrected spelling and added 'default' and 'max_length'
    delivery_radius = models.FloatField()  # Corrected spelling

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')  # Assume 'Profile' is defined elsewhere, changed related_name to 'orders'
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='orders')
    order_conformed = models.BooleanField(default=False)
    is_customer_delivered = models.BooleanField(default=False)  # Changed to 'is_customer_delivered' for clarity
    is_chef_delivered = models.BooleanField(default=False)  # Changed to 'is_chef_delivered' for clarity

