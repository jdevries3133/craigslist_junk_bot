from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile_setup
urlpatterns = [
    path('register/', register, name="regiseter"),
    path('setup/', profile_setup, name="profile_setup"),
    path('login/', LoginView.as_view(template_name='login.html')),
]