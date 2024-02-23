from django.db import models
from core.models import Photo, Profile, Chef


class Kitchen(models.Model):
    '''
    Kitchen to be regestered by chef and verified by admin
    '''
    name = models.TextField(blank=True)
    photos = models.ManyToManyField(Photo, related_name='kitchens', blank=True)
    is_verified = models.BooleanField(default=False)  
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='kitchens')  

class Dish(models.Model):  
    '''
    Dishes to be added by chef and verify by admin

    total_order should be appended +1 with each succesful order
    '''
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='dishes')
    description = models.TextField()  
    ingredients = models.TextField()
    recipe = models.TextField()
    photos = models.ManyToManyField(Photo, related_name='dishes', blank=True)
    is_verified = models.BooleanField(default=False)  
    price = models.FloatField()
    total_orders = models.IntegerField()

class Inventory(models.Model):
    '''
    Inventory (Live Dishes) are dished to be shown in feed.

    Each dish is associated with kitchen and kitchen with chef
    '''


    DELIVERY_CHOICES = [  
        ('Delivery', 'Delivery'),
        ('Collect', 'Collect'),
    ]

    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='inventory')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='inventory')  
    ready_at = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='Delivery')  
    delivery_radius = models.FloatField()  

class Order(models.Model):
    '''
    Order is initated by user from inventory

    Order to be conformed by chef
    inventory.quantity should be -1 automatically

    After completion of order chef is to manually complete delievered.
    User side completion is automatic, but can be over ride in complain section by user
    
    '''
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')  
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='orders')
    order_conformed = models.BooleanField(default=False)
    is_customer_delivered = models.BooleanField(default=False)  
    is_chef_delivered = models.BooleanField(default=False)  

