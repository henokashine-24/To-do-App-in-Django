from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import ToTask
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class ToTaskLogin(LoginView):
    template_name = 'ToDos/login.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse_lazy('task-list')


class ToTaskList( LoginRequiredMixin,ListView):
    model = ToTask
    context_object_name = 'task'

class ToTaskDetail(DetailView):
    model = ToTask

class ToTaskCreate(LoginRequiredMixin,CreateView):
    model = ToTask
    fields = '__all__'
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')

class ToTaskUpdate(LoginRequiredMixin,UpdateView):
    model = ToTask
    fields = '__all__'
    success_url = reverse_lazy('task-list')
class ToTaskDelete(LoginRequiredMixin,DeleteView):
    model = ToTask
    context_object_name = 'task'
    success_url =  reverse_lazy('task-list')


