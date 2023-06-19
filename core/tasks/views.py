from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import reverse
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
    success_url = reverse_lazy('tasks:task-list')

    def form_valid(self, form:AddTaskForm):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/tasks/"
    
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = []
   
    def get_success_url(self):
        return reverse_lazy('tasks:task-list')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.done = True 
        task.save()
        return super().form_valid(form)