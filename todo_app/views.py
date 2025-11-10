from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import Task
from todo_app.forms import TaskForm

def home(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo_app/index.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('home')
