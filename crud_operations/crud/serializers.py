from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, old_instance, newData):
        old_instance.name = newData.get('name', old_instance.name)
        old_instance.roll = newData.get('roll', old_instance.roll)
        old_instance.city = newData.get('city', old_instance.city)
        old_instance.save()
        return old_instance