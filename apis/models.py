from django.contrib.postgres.fields import ArrayField
from django.db import models
from django import forms
class DataValue(models.Model):
    limits=ArrayField(models.FloatField(),size=7,default=list)
    healthScore=ArrayField(models.IntegerField(),size=5,default=list)
    controlLimitType=models.IntegerField(default=1)

class Meter(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    value=models.FloatField()
    class Meta:
        ordering=['-created']

class ExcelFiles(models.Model):
    file_name=models.CharField(max_length=100)
    file=models.FileField(null=True, blank=True)

