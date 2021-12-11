from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UpdateUserForm,UpdateProfileForm,RegisterForm

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
        return render(request,'registration/signup.html', {'form': form})

        
@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
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