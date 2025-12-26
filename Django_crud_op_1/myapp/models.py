from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    price = models.IntegerField()
