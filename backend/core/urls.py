from django.urls import path
from .views import UserList, UserDetail, ProfileList, ProfileDetail, ChefList, ChefDetail, PhotoList, PhotoDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('chefs/', ChefList.as_view(), name='chef-list'),
    path('chefs/<int:pk>/', ChefDetail.as_view(), name='chef-detail'),
    path('photos/', PhotoList.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetail.as_view(), name='photo-detail'),
]