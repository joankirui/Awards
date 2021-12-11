from django.urls import path
from .import views
from django.conf.urls import url,include

urlpatterns=[
    path('profile/',views.profile, name='profile')
]