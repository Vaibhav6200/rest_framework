from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('studentAPI/', views.studentAPI.as_view(), name="studentAPI"),
    path('studentAPI/<int:pk>', views.studentAPI.as_view(), name="studentAPI"),
]