from django import forms

from django.contrib.auth.models import User
from .models import Profile,Post, Rating
from cloudinary.models import CloudinaryField
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.Enter a valid email address. ')

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name','prof_pic', 'bio','contact']

class PostForm(forms.ModelForm):
    photo = CloudinaryField('image')
    class Meta:
        model = Post
        fields = ['title','photo','description','url']

class RatingsForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ['design','usability','content']