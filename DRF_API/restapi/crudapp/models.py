from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()