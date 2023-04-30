from django.contrib import admin
from .models import *


class CustomStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
    list_display_links = ['id', 'name']

admin.site.register(Student, CustomStudent)
