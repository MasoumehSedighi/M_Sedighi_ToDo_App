from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddTaskForm
from .models import Task


# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name='tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form:AddTaskForm):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/tasks/"