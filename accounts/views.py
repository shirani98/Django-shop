from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from accounts.forms import UserCreationForm
from accounts.models import User

# Create your views here.
class Login(LoginView):
    template_name = 'accounts/login.html'
    
class Register(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    
