from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'index.html')


def getStudent(request, pk):
    model_instance_1 = Student.objects.get(id=pk)
    serializer_1 = StudentSerializer(model_instance_1)
    json_data = JSONRenderer().render(serializer_1.data)

    return HttpResponse(json_data, content_type="application/json")


def student_list(request):
    query_set_obj = Student.objects.all()
    serializer = StudentSerializer(query_set_obj, many=True)

    return JsonResponse(serializer.data, safe=False)