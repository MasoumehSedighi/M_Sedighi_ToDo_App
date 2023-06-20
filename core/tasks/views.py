from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from .forms import TaskCreateForm, TaskUpdateForm
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
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks:task-list')

    def form_valid(self, form:TaskCreateForm):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task-list')
    
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "tasks/task_update.html"
    
    def get_success_url(self):
        return reverse_lazy('tasks:task-list')
    
    
class TaskDoneView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("tasks:task-list")
    
    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.done = True
        object.save()
        return redirect(self.success_url)