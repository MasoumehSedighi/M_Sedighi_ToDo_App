from django.urls import path
from . import views
from django.contrib.auth import views as BaseView

app_name='accounts'

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.UserCreateView.as_view(), name="signup"),
]