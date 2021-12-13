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
from django.http import HttpResponseRedirect



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
        print(request.POST)
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('/')
    else:
        form = PostForm()

    try:
        posts = Post.objects.all().order_by("date")
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]

    except Post.DoesNotExist:
        posts = None


    
    return render(request,'index.html',{"title":title,"posts":posts,"random_post":random_post,"form": form})

def calculate_rating(post):
    all_ratings = Rating.objects.filter(post=post)
    print(all_ratings)

    design_ratings = [design_rating.design for design_rating in all_ratings]
    design_average = sum(design_ratings) / len(design_ratings)

    usability_ratings = [usability_rating.usability for usability_rating in all_ratings]
    usability_average = sum(usability_ratings) / len(usability_ratings)

    content_ratings = [content_rating.content for content_rating in all_ratings]
    content_average = sum(content_ratings) / len(content_ratings)


    params = {
        "design_average": design_average,
        "usability_average": usability_average,
        "content_average": content_average
    }

    return params

@login_required(login_url='/accounts/login/')
def single_project(request,post):
    post = Post.objects.get(title=post)
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    user_rating = False
    if ratings is not None:
        user_rating = True

    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()

            average_rates = calculate_rating(post)
            print(average_rates)
            rate.design_average = average_rates.get("design_average")
            rate.usability_average = average_rates.get("usability_average")
            rate.content_average = average_rates.get("content_average")

            rate.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form = RatingsForm()


    return render(request,'project.html',{"form":form,"user_rating":user_rating,"post":post})





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
            return redirect('profile')
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
