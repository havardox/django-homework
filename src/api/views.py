from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HomeworkSerializer, StudentSerializer, GradeSerializer

from .models import Homework, Student, Grade


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Homework List': '/homeworks/',
        'Homework Detail View': '/homeworks/<str:pk>/',
        'Homework Create': '/homework-create/',
        'Homework Update': '/homeworks/<str:pk>/update/',
        'Homework Delete': '/homeworks/<str:pk>/delete/',
        'Student List': '/students/',
        'Student Detail View': '/students/<str:pk>/',
        'Student Create': '/student-create/',
        'Student Update': '/students/<str:pk>/update/',
        'Student Delete': '/students/<str:pk>/delete/',
        'Grade List': '/grades/',
        'Grade Detail View': '/grades/<str:pk>/',
        'Grade Create': '/grade-create/',
        'Grade Update': '/grades/<str:pk>/update/',
        'Grade Delete': '/grades/<str:pk>/delete/',
    }
    return Response(api_urls)


def object_list(Model, Serializer):
    objects = Model.objects.all()
    serializer = Serializer(objects, many=True)
    return Response(serializer.data)


def object_detail(pk, Model, Serializer):
    obj = Model.objects.get(id=pk)
    serializer = Serializer(obj, many=False)
    return Response(serializer.data)


def object_create(request, Serializer):
    serializer = Serializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


def object_update(request, pk, Model, Serializer):
    obj = Model.objects.get(id=pk)
    serializer = Serializer(instance=obj, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


def object_delete(pk, Model):
    obj = Model.objects.get(id=pk)
    obj.delete()
    return Response(f'{Model.__name__} successfully deleted!')


@api_view(['GET'])
def homework_list(request):
    return object_list(Homework, HomeworkSerializer)


@api_view(['GET'])
def homework_detail(request, pk):
    return object_detail(pk, Homework, HomeworkSerializer)


@api_view(['POST'])
def homework_create(request):
    return object_create(request, HomeworkSerializer)


@api_view(['POST'])
def homework_update(request, pk):
    return object_update(request, pk, Homework, HomeworkSerializer)


@api_view(['DELETE'])
def homework_delete(request, pk):
    return object_delete(pk, Homework)


@api_view(['GET'])
def student_list(request):
    return object_list(Student, StudentSerializer)


@api_view(['GET'])
def student_detail(request, pk):
    return object_detail(pk, Student, StudentSerializer)


@api_view(['POST'])
def student_create(request):
    return object_create(request, StudentSerializer)


@api_view(['POST'])
def student_update(request, pk):
    return object_update(request, pk, Student, StudentSerializer)


@api_view(['DELETE'])
def student_delete(request, pk):
    return object_delete(pk, Student)


@api_view(['GET'])
def grade_list(request):
    return object_list(Grade, GradeSerializer)


@api_view(['GET'])
def grade_detail(request, pk):
    return object_detail(pk, Grade, GradeSerializer)


@api_view(['POST'])
def grade_create(request):
    return object_create(request, GradeSerializer)


@api_view(['POST'])
def grade_update(request, pk):
    return object_update(request, pk, Grade, GradeSerializer)


@api_view(['DELETE'])
def grade_delete(request, pk):
    return object_delete(pk, Grade)
