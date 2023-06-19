from django.urls import path
from . import views
from django.contrib.auth import views as BaseView


app_name='tasks'

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("add/",views.TaskCreateView.as_view(), name="task-add"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update")
]