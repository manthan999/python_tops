from django.db import models

# Create your models here.

class student (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()

class employee (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.FloatField(max_length=20)
