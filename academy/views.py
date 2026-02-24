from django.shortcuts import render

from .models import Course, Student, Trainer

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)

def trainer_list(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers,
    }
    return render(request, 'trainers.html', context)

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students.html', context)