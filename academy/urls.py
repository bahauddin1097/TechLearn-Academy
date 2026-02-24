from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.course_list, name='courses'),
    path('trainers/', views.trainer_list, name='trainers'),
    path('students/', views.student_list, name='students')
]