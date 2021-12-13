from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from awardsapp.models import Post
from .serializers import PostSerializer, ProfileSerializer
from .forms import UpdateUserForm,UpdateProfileForm,RegisterForm,PostForm,RatingsForm
from rest_framework.generics import ( ListAPIView)
from .models import Profile,Post,Rating
import random


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
def index(request):
    title = "Welcome to awards"
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            import pdb
            pdb.set_trace()
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all().order_by("date")
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]

    except:
        pass


    
    return render(request,'index.html',{"title":title,"posts":posts,"random_post":random_post,"form": form})

@login_required(login_url='/accounts/login/')
def post_project(request):


    return render(request,'project.html')


@login_required(login_url='/accounts/login/')
def logout_then_login(request):
     return render(request,'registration/login.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'profile.html')


def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)

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

class PostViews(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("date")
