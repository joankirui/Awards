from rest_framework import  serializers
from .models import Post, Profile,User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email']
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['prof_pic','bio','contact','name','user']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','photo','description','url','date']




