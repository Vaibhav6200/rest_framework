from django.db import models


class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)