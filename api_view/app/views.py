from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer


# @api_view()
# def index(request):
#     return Response({'msg': "hello vaibhav"})

# @api_view(['GET'])
# def index(request):
#     return Response({'msg': "hello vaibhav"})

# @api_view(['POST'])
# def index(request):
#     if request.method == "POST":
#         print(request.data)
#         print(type(request.data))
#         return Response({'msg': "This is a Post Request"})

# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == "GET":
#         return Response({'msg': "Message from GET method"})
#     if request.method == "POST":
#         return Response({'msg': "This is POST method"})


@api_view(['GET', 'POST', 'PUT', "PATCH", 'DELETE'])
def index(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'data inserted Successfully'}, status=201)
        return Response(serializer.errors, status=400)

    if request.method == "PUT":
        id = request.data.get('id', None)
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(instance=stud, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updation Successfull"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg": "deletion Successfull"})