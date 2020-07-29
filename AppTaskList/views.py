from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Description
from .forms import TaskForm, DescriptionForm
from django.views.generic import TemplateView, FormView

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

'''class createDescriptions(FormView):
    form_class = DescriptionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        desc = Task.objects.get(pk=self.kwargs['pk'])
        context['desc'] = desc
        return context

    def form_valid (self, form):
        pk = self.kwargs['pk']
        dados = form.clean()
        task_id = Task.objects.get(id=pk)
        description = Description(description=dados['description'])
        description.save()
'''

def details (request, pk):
    try:
        description = Description.objects.get(id=pk)
        task = Task.objects.get(description=pk)

    except Exception as identifier:
        pass
    return render(request, 'AppTaskList/details.html', {'task':task, 'description':description})