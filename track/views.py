from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Track
from .serializers import TrackSerial
# Create your views here.


class TrackView(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerial


class TrackCreate(generics.CreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerial


class TrackRetrieve(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerial


class TrackUpdate(generics.UpdateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerial


class TrackDelete(generics.DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerial


