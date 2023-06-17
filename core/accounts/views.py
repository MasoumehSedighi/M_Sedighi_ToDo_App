from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import RegisterForm

# Create your views here.


class UserCreateView(CreateView):
    model = User
    template_name = "accounts/signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')