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
    name = models.CharField(blank=True,max_length=100)

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
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    def save_post(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        return cls.objects.filter(title__icontains=search_term)

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

class Rating(models.Model):
    rating = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10')]

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    def __str__(self):
        return f'{self.post}Rating'

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

