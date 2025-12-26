"""
Docstring for backend.api.views

## Handles 'Get all text' and 'Save new next'. 
Using Django REST Framework saves CPU cycles
"""
from django.shortcuts import render
from rest_framework import generics
from .models import TextDocument
from .serializers import TextSerializer

# Create your views here.
class TextListCreate(generics.ListCreateAPIView):
    queryset = TextDocument.objects.all()
    serializer_class = TextSerializer