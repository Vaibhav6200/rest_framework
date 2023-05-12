from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from .models import *

# ListAPIView
# CreateAPIView
# RetrieveAPIView
# UpdateAPIView
# DestroyAPIView

# class StudentAPI(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPI(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPI(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPI(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPI(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class LC_StudentAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUD_StudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

