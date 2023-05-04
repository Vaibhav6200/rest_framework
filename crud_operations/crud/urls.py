from django.urls import path
from . import views


urlpatterns = [
    path('get_student/', views.get_student, name="get_student"),
]
