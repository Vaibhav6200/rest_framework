from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_student(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)        # get Complex Data
            serializer = StudentSerializer(stu)      # serialize complex data into python object
            return JsonResponse(data=serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)

        serializer = StudentSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Data Created"}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythonData, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {"message": "Data Updated !!!"}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors, safe=False)

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg": "Student Deleted"}
        return JsonResponse(res, safe=False)
