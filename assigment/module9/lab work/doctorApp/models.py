from django.db import models

# Create your models here.

class Doctor(models.Model):
    docName = models.CharField(max_length=25, default="default")
    docSpecialization = models.CharField(max_length=25, default="default")
    docHospital = models.CharField(max_length=25, default="default")
    docExperience = models.IntegerField(default=999)

