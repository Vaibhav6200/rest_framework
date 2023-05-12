from django.contrib import admin
from .models import *

class CustomStudent(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name', 'city']
    list_display_links = ['id', 'roll', 'name']

admin.site.register(Student, CustomStudent)