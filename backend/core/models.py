from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey ,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    '''
    Added features on django User Model

        Chef_mode : to be activated for intrested chefs
    '''

    user_id = models.OneToOneField(UserAccount, related_name='Profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profil_pic', blank=True)
    chef_mode = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile of {self.user_id.first_name}"


class Chef(models.Model):
    '''
    Added features on django User Model again (Merge with profile if you need)

        Extra fields for chef profiles.

        is_verified : To be verified by admin
    '''
    
    user_id = models.OneToOneField(Profile, related_name='Profile', on_delete=models.CASCADE)
    description = models.CharField(max_length = 500, blank=True)
    is_verified = models.BooleanField(default=False)
    photos = models.ManyToManyField('Photo', related_name='chefs', blank=True)

    def __str__(self):
        return f" Chef :  {self.user_id.user_id.first_name}"

class Photo(models.Model):
    '''
    Generic model for photos
    '''
    photo = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)


from django.contrib.auth import get_user_model
User = get_user_model()


class Like(models.Model):
    '''
    Like model is generic model, any other model can have like functinality by inheriting folling model, see documentation
    '''
    
    # Generic Foreign Key to associate comments with different models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Model specific fields
    user = models.ForeignKey(User, on_delete=models.CASCADE )

    class Meta:
        unique_together = (("content_type", "object_id", "user"),)

    def save(self, *args, **kwargs):
        existing_like = Like.objects.filter(
            content_type=self.content_type,
            object_id=self.object_id,
            user=self.user
        )
        if existing_like.exists():
            raise ValidationError("You have already liked this content.")
        else:
            super(Like, self).save(*args, **kwargs)

class Likable(models.Model):
    likes = GenericRelation(Like)
    class Meta:
        abstract = True


class Review(Likable):
    '''
    Review model is generic model, any other model can have review/comment functinality by inheriting folling model, see documentation
    '''

    # Generic Foreign Key to associate comments with different models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Self-referencing field for replies to comments
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    # Model specific fields
    creator = models.ForeignKey(User, on_delete=models.CASCADE )
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Reviewable(models.Model):
    comments = GenericRelation(Review)
    class Meta:
        abstract = True