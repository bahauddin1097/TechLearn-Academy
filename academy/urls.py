from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.courses_list, name='courses'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/<int:id>/edit', views.edit_course, name='edit_course'),
    path('courses/<int:id>/delete/', views.delete_course, name='delete_course'),

    path('trainers/', views.trainers_list, name='trainers'),
    path('trainers/<int:id>/', views.trainer_detail, name='trainer_detail'),
    path('trainers/add/', views.add_trainer, name='add_trainer'),
    path('trainers/<int:id>/edit', views.edit_trainer, name='edit_trainer'),
    path('trainers/<int:id>/delete', views.delete_trainer, name='delete_trainer'),
    
    path('students/', views.students_list, name='students'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:id>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:id>/delete/', views.delete_student, name='delete_student')
]