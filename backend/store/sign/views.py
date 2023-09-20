from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User
from shop.models import CustomUser
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm


class BaseRegisterView(CreateView):
    # model = User
    # model = CustomUser
    form_class = BaseRegisterForm
    # form_class = CustomUserCreationForm
    success_url = '/'


class LoginViewCustom(LoginView):
    form_class = CustomAuthenticationForm