from django.urls import path
from .import views

app_name='restApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('studentList/', views.studentList, name="studentList"),
    path('studentList/<int:pk>', views.getStudent, name="getStudent"),
    path('createStudent/', views.createStudent, name="createStudent"),
]
