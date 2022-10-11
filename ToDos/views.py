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
    fields = ['title', 'description','complete'] 

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count'] = context['task'].filter(complete=False).count()


        search_input = self.request.GET.get('search-area') or '' # we are applying a search functionality to the page..

        if search_input:
            context['task'] = context['task'].filter(title__icontains = search_input)

        context['search_input'] = search_input  # search functionality ends here..



        return context

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


