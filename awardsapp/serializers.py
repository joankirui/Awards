from rest_framework import  serializers
from .models import Profile,User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email']
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['prof_pic','bio','contact','name','user']





