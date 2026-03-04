from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Course, Trainer, Student

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'name', 'display_groups', 'is_staff']

    def name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def display_groups(self, obj):
        return ', '.join(group.name for group in obj.groups.all())
    
    display_groups.short_description = 'Groups'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'short_description', 'duration']
    list_display_links = ['name',]
    ordering = ['name',]
    search_fields = ['name',]

    def short_description(self, obj):
        return obj.description[:70]


class TrainerAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name', 'email', 'expertise']
    list_display_links = ['name',]
    ordering = ['first_name',]
    search_fields = ['name', 'email', 'expertise']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'enrolled_course', 'trainer', 'is_active']
    ordering = ['first_name',]
    search_fields = ['name', 'email']

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)