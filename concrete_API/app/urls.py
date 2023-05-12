from django.urls import path
from . import views


urlpatterns = [
    path("app/", views.LC_StudentAPI.as_view()),
    path("app/<int:pk>/", views.RUD_StudentAPI.as_view()),
]
