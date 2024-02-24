from django.contrib import admin
from .models import Profile, Chef, Photo, Like, Review,UserAccount  
from django.contrib.auth.admin import UserAdmin

class UserAccountAdmin(UserAdmin):
    # Define list_display to control which fields are displayed on the admin change list page.
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    # Define fieldsets to control the layout of admin “add” and “change” pages.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Register your models here.
admin.site.register(UserAccount, UserAccountAdmin)


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
