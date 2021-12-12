from django.urls import path
from django.contrib import admin
from .import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('profile/',views.profile, name='profile'),
    path('update/',views.edit_profile, name='edit'),
    path('api/profile',views.ProfileViews.as_view(),name='profileapi'),
    path('api/posts', views.PostViews.as_view(),name='postsapi'),

]
if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)