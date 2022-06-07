# from django.shortcuts import render
from rest_framework import viewsets  
from .serializers import LibrarySerializer
from .models import librarybooks


# Create your views here.
class LibraryViewSet(viewsets.ModelViewSet):
    queryset=librarybooks.objects.all().order_by('title'),
    serializer_class=LibrarySerializer

