from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=20)

class country (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class state (models.Model):
    country = models.ForeignKey(country,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class city (models.Model):
    state = models.ForeignKey(state,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
