# from django.shortcuts import render
# # from django.http import HttpResponse
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView

# from .models import Task


# # Create your views here.
# class taskList(ListView):
#     # return HttpResponse('To Do list') 
#     model = Task
#     context_object_name = 'tasks'


# class TaskDetail(DetailView):
#     model = Task
#     # context_object_name = 'task'



from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'base/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')



