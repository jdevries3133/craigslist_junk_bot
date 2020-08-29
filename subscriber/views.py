from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
def register(request, *args, **kwargs):
    """
    This ain't right
    """
    return render(request, 'register.html')