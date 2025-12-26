"""
Converts MongoDB documents into JSON so Flask frontend can read 
"""
from rest_framework import serializers
from .models import TextDocument

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextDocument
        fields = ['id', 'content', 'created_at']