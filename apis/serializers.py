from django.contrib.postgres import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import DataValue, ExcelFiles, Meter
from django.forms import ModelForm
class DataValueSerializer(ModelSerializer):
    class Meta:
        model=DataValue
        fields='__all__'

class MeterSerializer(ModelSerializer):
    class Meta:
        model=Meter
        fields='__all__'

class ExcelFilesSerializer(ModelSerializer):
    class Meta:
        model=ExcelFiles
        fields='__all__'
        
        