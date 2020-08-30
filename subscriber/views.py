from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProfileSetupForm

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('profile_setup'), permanent=True)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# @login_required(login_url="/login/")
def profile_setup(request):
    if request.method == 'POST':
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            form.save()
            request.user.SubscriberProfile.is_profile_setup = True
            return redirect(reverse('install_app_now'), permanent=True)
    else:
        form = ProfileSetupForm()
    return render(request, 'profile.html', {'form': form})

# @login_required(login_url="/login/")
def install_app_now(request):
    if not request.User.SubscriberProfile.is_profile_setup:
        return redirect(reverse('profile_setup')) # also, cause a notification popup that says, "please set your shit up first"
    pass