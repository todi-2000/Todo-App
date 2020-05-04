from django.shortcuts import render
from django.http import JsonResponse
from .models import Notes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NotesSerializers

# Create your views here.
@api_view(['GET'])
def AppOverview(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def noteslist(request):
    notes= Notes.objects.all()
    serializers= NotesSerializers(notes,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def notesdetails(request,pk):
    notes= Notes.objects.get(id=pk)
    serializers= NotesSerializers(notes,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def notescreate(request):
    serializers=NotesSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def notesupdate(request,pk):
    notes=Notes.objects.get(id=pk)
    serializers=NotesSerializers(instance=notes,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def notesdelete(request,pk):
    notes=Notes.objects.get(id=pk)
    notes.delete()
    return Response(serializers.data)