from django.urls import path
from . import views
from django.contrib.auth import views as BaseView


app_name='tasks'

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("task/add/",views.TaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/done/", views.TaskDoneView.as_view(), name="task-done")
]