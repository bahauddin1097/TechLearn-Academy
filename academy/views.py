from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .models import Course, Trainer, Student
from .forms import CourseForm, TrainerForm, StudentForm

# Create your views here.
# Courses view
def courses_list(request):
    courses = Course.objects.all().order_by('name')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courses.html', context)

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course': course,
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
@permission_required('academy.add_course', raise_exception=True)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    form = CourseForm()
    context = {
        'form': form,
    }
    return render(request, 'courses/add_course.html', context)

@login_required
@permission_required('academy.edit_course', raise_exception=True)
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    form = CourseForm(instance=course)
    context = {
        'course': course,
        'form': form
    }
    return render(request, 'courses/edit_course.html', context)

@login_required
@permission_required('academy.delete_course', raise_exception=True)
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    form = CourseForm(instance=course)
    context = {
        'form': form,
        'course': course
    }
    return render(request, 'courses/delete_course.html', context)

# Trainers view
def trainers_list(request):
    trainers = Trainer.objects.all().order_by('first_name')
    context = {
        'trainers': trainers,
    }
    return render(request, 'trainers/trainers.html', context)

@login_required
def trainer_detail(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    context = {
        'trainer': trainer,
    }
    return render(request, 'trainers/trainer_detail.html', context)

@login_required
@permission_required('academy.add_trainer', raise_exception=True)
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    form = TrainerForm()
    context = {
        'form': form,
    }
    return render(request, 'trainers/add_trainer.html', context)

@login_required
@permission_required('academy.edit_trainer', raise_exception=True)
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    form = TrainerForm(instance=trainer)
    context = {
        'form': form,
        'trainer': trainer
    }
    return render(request, 'trainers/edit_trainer.html', context)

@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainers')
    form = TrainerForm(instance=trainer)
    context = {
        'form': form,
        'trainer': trainer
    }
    return render(request, 'trainers/delete_trainer.html', context)

# Students view
def students_list(request):
    students = Student.objects.all().order_by('first_name')
    context = {
        'students': students,
    }
    return render(request, 'students/students.html', context)

def is_trainer(user):
    if user.groups.filter(name='Trainer').exists():
        return True
    raise PermissionDenied

@login_required
@user_passes_test(is_trainer)
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context)

@login_required
@permission_required('academy.add_student', raise_exception=True)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    form = StudentForm()
    context = {
        'form': form,
    }
    return render(request, 'students/add_student.html', context)

@login_required
@permission_required('academy.edit_student', raise_exception=True)
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/edit_student.html', context)

@login_required
@permission_required('academy.delete_student', raise_exception=True)
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('students')
    form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/delete_student.html', context)