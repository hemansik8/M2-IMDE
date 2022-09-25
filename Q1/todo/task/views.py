from multiprocessing import context, reduction
import re
from turtle import update
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import tasks, person
from .forms import taskForms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    try:
        data = person.objects.all()
        context = {"person" : data}
    except Exception as e:
        context = {"person": "No user found..."}
    return render(request, 'index.html')

def tasks(request):
    try:
        data = tasks.objects.all()
        context = {"task" : data}
    except Exception as e:
        context = {"task": "No tasks found..."}
    return render(request, 'tasks.html')

def taskDetails(request, pm):
    fetchData = tasks.objects.get(name = pm)
    print(fetchData)
    context = {"fetchData":fetchData}
    return render(request, 'taskDetails.html', context)

def taskAdd(request):
    form = taskForms()
    context = {'forms' : form}
    return render(request, 'taskAdd.html', context)

def taskAdd(request):
    form = taskForms()
    if request.method == 'POST':
         myData = taskForms(request.POST)
         if myData.is_valid():
            myData.save()
            messages.success(request, 'Project Added Successfully')
            return redirect('task')
    context = {'forms' : form}
    return render(request, 'taskAdd.html', context)

def taskDelete(request, id):
    data = tasks.objects.get(id = id)
    data.delete()
    return redirect('tasks')

def taskUpdate(request, id):
    myData = tasks.objects.get(id = id)
    updateForm = taskForms(request.POST or None, instance = myData)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('tasks')
    context = {'form' : updateForm}
    return render(request, 'taskUpdate.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['Password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Credentials are incorrect")
            return redirect('home')
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('home') 

def signup(request):
    return render(request, 'signup.html')

def contact(request):
    return render(request, 'contact.html')