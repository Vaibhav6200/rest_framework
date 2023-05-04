from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer
from rest_framework.views import APIView


class studentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'data inserted Successfully'}, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, format=None):
        id = request.data.get('id', None)
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(instance=stud, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updation Successfull"})
        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg": "deletion Successfull"})