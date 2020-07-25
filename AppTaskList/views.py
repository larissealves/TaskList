from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Description
from .forms import TaskForm, DescriptionForm


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'AppTaskList/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'AppTaskList/updateTask.html', context)

def deleteTask (request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'AppTaskList/delete.html', context)

def createDescriptions(request):
    descrip = Description.objects.all()

    form = DescriptionForm()

    if request.method == "POST":
        form = DescriptionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'descrip':descrip, 'form':form}
    return render(request, 'AppTaskList/createForm.html', context)

def details (request, pk):
    try:
        description = Description.objects.get(id=pk)
        task = Task.objects.get(description=pk)

    except Exception as identifier:
        pass
    return render(request, 'AppTaskList/details.html', {'task':task, 'description':description})