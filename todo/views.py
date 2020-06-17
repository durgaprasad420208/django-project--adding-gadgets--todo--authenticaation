from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm

# Create your views here.


def todo_home(request):
    task = TaskList.objects.all()
    context = {"task": task}
    return render(request, 'todo/todo_home.html', context)


def todo_retrive(request, id):
    title = "Detailed task"
    task = TaskList.objects.get(pk=id)
    template = "todo/todo_retrive.html"
    context = {"title": title, "task": task}
    return render(request, template, context)


def todo_create(request):
    title = "Create Task"
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect('todo-home')
    else:
        form = TaskForm()
    template = "todo/todo_create.html"
    context = {
        "title": title,
        "form": form
    }
    return render(request, template, context)


def todo_edit(request, id):
    title = "Edit your task"
    task = TaskList.objects.get(pk=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('todo-home')

    template = "todo/todo_edit.html"
    context = {"title": title, "form": form}
    return render(request, template, context)


def todo_delete(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    return redirect('todo-home')
