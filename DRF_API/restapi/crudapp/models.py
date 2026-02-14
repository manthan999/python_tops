from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)

class Author(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image =models.ImageField(upload_to="images",null=True)