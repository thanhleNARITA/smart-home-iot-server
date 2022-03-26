from rest_framework import serializers
from .models import RoomButton, Todolist, RoomStatus

class RoomButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomButton
        fields = ('led_status', 'door_status', 'esaving_status',
                  'aircon_status')

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id','title', 'date')

class RoomStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = ('id', 'temperature', 'pressure', 'humidity')

        def __str__(self):

            return self.model.temperature, self.model.pressure,self.model.humidity