from rest_framework import serializers
from .models import Profile, Chef, Photo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user_id', 'profile_pic', 'chef_mode']

class ChefSerializer(serializers.ModelSerializer):
    user_id = ProfileSerializer(read_only=True)
    photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Chef
        fields = ['user_id', 'description', 'is_verified', 'photos']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo', 'caption']
