from dataclasses import fields
from rest_framework import serializers
from .models import librarybooks

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=librarybooks
        fields='__all__'
