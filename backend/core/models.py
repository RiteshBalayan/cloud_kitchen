from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey ,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Profile(models.Model):
    '''
    Added features on django User Model

        Chef_mode : to be activated for intrusted chefs
    '''

    user_id = models.OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profil_pic', blank=True)
    chef_mode = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile of {self.user_id.username}"


class Chef(models.Model):
    '''
    Added features on django User Model again (Merge with profile if you need)

        Extra fields for chef profiles.

        is_verified : To be verified by admin
    '''
    
    user_id = models.OneToOneField(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 500, blank=True)
    is_verified = models.BooleanField(default=False)
    photos = models.ManyToManyField('Photo', related_name='chefs', blank=True)

class Photo(models.Model):
    '''
    Generic model for photos
    '''
    photo = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)

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