from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Task


# Create your views here.
class taskList(ListView):
    # return HttpResponse('To Do list') 
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'




