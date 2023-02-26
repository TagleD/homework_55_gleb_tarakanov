from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.db import DataBase
from webapp.forms import TaskForm
from webapp.models import Task

def tasks_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context=context)

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_detail.html', context=context)


def add_view(request: WSGIRequest):
    # GET
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add_task.html', context={
            'form': form
        })

    # POST
    form = TaskForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'add_task.html', context={
            'form': form
        })

    # Success
    else:
        task = Task.objects.create(**form.cleaned_data)
        return redirect(f'/task?pk={task.pk}')


def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'ended_at': task.ended_at
        })
        return render(request, 'update_task.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status'],
            task.ended_at = form.cleaned_data['ended_at']
            task.save()
            return redirect(f'/task?pk={task.pk}')
        else:
            return render(request, 'update_task.html', context={'form': form, 'task': task})

