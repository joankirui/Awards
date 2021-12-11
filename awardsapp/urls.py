from django.urls import path
from django.contrib import admin
from .import views
from django.conf.urls import url,include
from django_registration.backends.one_step.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('profile/',views.profile, name='profile'),
    path('update/',views.edit_profile, name='edit'),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
]
if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)