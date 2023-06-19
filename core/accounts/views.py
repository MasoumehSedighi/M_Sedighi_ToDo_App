from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import User
from .forms import RegisterForm

# Create your views here.

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "email", "password"
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks:task_list")
    

class UserCreateView(CreateView):
    model = User
    template_name = "accounts/signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')


