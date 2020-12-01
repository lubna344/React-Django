import tutorials
from django.shortcuts import render
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        tutorial = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorial, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = TutorialSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorials = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TutorialSerializer(tutorials)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TutorialSerializer(tutorials, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorials.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 
    # GET / PUT / DELETE tutorial
                
@api_view(['GET'])
def tutorial_list_published(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = TutorialSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

