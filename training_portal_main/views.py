from django.shortcuts import render

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