from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    prof_pic = CloudinaryField('image')
    bio = models.CharField(max_length=30,blank=True,null=True)
    contact = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.user.username}Profile'

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Post(models.Model):
    title = models.CharField(max_length=50)
    photo = CloudinaryField('image')
    description = models.TextField(max_length=255)
    url = models.URLField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return f'{self.title}'
