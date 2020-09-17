from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HomeworkSerializer

from .models import Homework


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/homework-list/',
        'Detail View': '/homework-detail/<str:pk>/',
        'Create': '/homework-create/',
        'Update': '/homework-update/<str:pk>/',
        'Delete': '/homework-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def homework_list(request):
    homeworks = Homework.objects.all()
    serializer = HomeworkSerializer(homeworks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def homework_detail(request, pk):
    homework = Homework.objects.get(id=pk)
    serializer = HomeworkSerializer(homework, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def homework_create(request):
    serializer = HomeworkSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def homework_update(request, pk):
    homework = Homework.objects.get(id=pk)
    serializer = HomeworkSerializer(instance=homework, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def homework_delete(request, pk):
    homework = Homework.objects.get(id=pk)
    homework.delete()
    return Response('Homework successfully deleted!')
