from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from awardsapp.models import Post
from .serializers import ProfileSerializer
from .forms import UpdateUserForm,UpdateProfileForm,RegisterForm
from rest_framework.generics import (GenericAPIView, ListAPIView,RetrieveAPIView)
from .models import Profile,Post

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get['email']
            username = form.cleaned_data.get('username')

            messages.success(request,f'Account for {username} created,you can now login')
            return redirect('login')
        else:
            form = RegisterForm()
        return render(request,'django_registration/registration_form.html', {'form': form})



@login_required(login_url='/accounts/login/')
def logout_then_login(request):
     return render(request,'registration/login.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    args = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit.html', args)

def search_project(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        results = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"results":results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

class ProfileViews(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    