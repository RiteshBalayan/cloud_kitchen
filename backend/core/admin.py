from django.contrib import admin
from .models import Profile, Chef, Photo, Like, Review  

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user_id']

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    search_fields = ['user_id']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption']
    search_fields = ['caption']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'user']
    search_fields = ['user__username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['creator', 'review', 'created']
    search_fields = ['creator__username', 'review']
    list_filter = ['created']
