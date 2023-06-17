from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import AddTaskForm
from .models import Task


# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    queryset = Task.objects.all()
    template_name='tasks/task_list.html'

    
class TaskCreateView(CreateView):
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/tasks/"