from rest_framework import serializers
from .models import Profile, Chef, Photo
#from django.contrib.auth.models import User

from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email']

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
