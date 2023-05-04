from django.urls import path
from . import views

app_name = "validation"

urlpatterns = [
    path("", views.index, name="index")
]
