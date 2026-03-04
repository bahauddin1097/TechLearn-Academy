from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

from django.shortcuts import redirect, render

from academy.models import Course, Student, Trainer

def home(request):
    courses = Course.objects.all().count()
    trainers = Trainer.objects.all().count()
    students = Student.objects.all().count()
    context = {
        'courses': courses,
        'trainers': trainers,
        'students': students,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'register/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'register/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('login')