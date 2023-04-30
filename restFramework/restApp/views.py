from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


def getStudent(request, pk):
    model_instance_1 = Student.objects.get(id=pk)
    serializer_1 = StudentSerializer(model_instance_1)
    json_data = JSONRenderer().render(serializer_1.data)

    return HttpResponse(json_data, content_type="application/json")


def studentList(request):
    query_set_obj = Student.objects.all()
    serializer = StudentSerializer(query_set_obj, many=True)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def createStudent(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)