from django.urls import path
from .import views

app_name='restApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('studentList/', views.student_list, name="student_list"),
    path('studentList/<int:pk>', views.getStudent, name="getStudent"),
]
