from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class LoginViewCustom(LoginView):
    form_class = CustomAuthenticationForm