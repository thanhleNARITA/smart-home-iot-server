from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializers import RoomButtonSerializer, TodolistSerializer, RoomStatusSerializer
from .models import RoomButton, Todolist, RoomStatus
from rest_framework.parsers import JSONParser
from django.views.decorators.http import condition
from django.http import StreamingHttpResponse
import json
import time
# Create your views here.


@api_view(['GET'])
def taskList(request):
    room = RoomButton.objects.all()
    serializer = RoomButtonSerializer(room, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    room = RoomButton.objects.get(id=pk)
    serializer = RoomButtonSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = RoomButtonSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    room = RoomButton.objects.get(id=pk)
    serializer = RoomButtonSerializer(instance=room,
                                      data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#================Todolist==================#
@api_view(['GET'])
@parser_classes([JSONParser])
def todolist_view(request, format=None):
    todolist = Todolist.objects.all()
    serializer = TodolistSerializer(todolist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def todolist_detail(request, pk):
    todolist = Todolist.objects.get(id=pk)
    serializer = TodolistSerializer(todolist, many=False)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@parser_classes([JSONParser])
def todolist_create_new(request):
    serializer = TodolistSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def todolist_update(request, pk):
    todolist = Todolist.objects.get(id=pk)
    serializer = TodolistSerializer(instance=todolist,
                                      data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE', 'GET', 'POST'])
def todolist_delete(request, pk):
    todolist = Todolist.objects.get(id = pk)
    todolist.delete()
    serializer = TodolistSerializer(todolist, many=False)
    return Response(serializer.data)

#==================RoomStatus(Temperature, Pressure, Humidity)================================#
@api_view(['GET'])
@parser_classes([JSONParser])
def roomstatus_view(request, format=None):
    roomstatus = RoomStatus.objects.all()
    serializer = RoomStatusSerializer(roomstatus, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def roomstatus_view_detail(request, pk):
    roomstatus = RoomStatus.objects.get(id=pk)
    serializer = RoomStatusSerializer(roomstatus, many=False)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@parser_classes([JSONParser])
def roomstatus_create_new(request):
    serializer = RoomStatusSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@parser_classes([JSONParser])
def roomstatus_update(request, pk):
    roomstatus = RoomStatus.objects.get(id=pk)
    serializer = RoomStatusSerializer(instance=roomstatus,
                                      data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE', 'GET', 'POST'])
def roomstatus_delete(request, pk):
    roomstatus = RoomStatus.objects.get(id = pk)
    roomstatus.delete()
    serializer = TodolistSerializer(roomstatus, many=False)
    return Response(serializer.data)

@condition(etag_func=None)
def stream_response(request):
    resp = StreamingHttpResponse(stream_response_generator(request), content_type='text/event-stream')
    return resp


def stream_response_generator(request):
    roomstatus = RoomStatus.objects.get(id=1)
    serializer = RoomStatusSerializer(instance=roomstatus)
    id_dics = serializer.data["id"]
    temp_dics = serializer.data["temperature"]
    pressure_dics = serializer.data["pressure"]
    humidity_dics = serializer.data["humidity"]
    id = f'"id":"{id_dics}"'
    temperature = f'"temperature":"{temp_dics}"'
    pressure = f'"pressure":"{pressure_dics}"'
    humidity = f'"humidity":"{humidity_dics}"'
    string = "{" + id + "," + temperature + "," + pressure + "," + humidity + "}"


    yield "data: %s\n" "retry:4000\n\n" % string
