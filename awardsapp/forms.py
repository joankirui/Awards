from django import forms

from django.contrib.auth.models import User
from .models import Profile,Post
from cloudinary.models import CloudinaryField

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.Enter a valid email address. ')

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name','prof_pic', 'bio','contact']