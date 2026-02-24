from django.contrib import admin

from .models import Course, Trainer, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_image', 'course_name', 'short_description', 'duration']
    list_display_links = ['course_name']
    ordering = ['course_name',]
    search_fields = ['course_name',]

    def short_description(self, obj):
        return obj.description[:70]


class TrainerAdmin(admin.ModelAdmin):
    list_display = ['trainer_photo', 'name', 'email', 'expertise']
    list_display_links = ['name']
    ordering = ['first_name',]
    search_fields = ['name', 'email', 'expertise']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'enrolled_course', 'trainer', 'is_active']
    ordering = ['first_name']
    search_fields = ['name', 'email']

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)