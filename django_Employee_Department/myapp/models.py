from django.db import models

# Create your models here.
 
class Department(models.Model):
    name = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name

class Employee(models.Model):
    Department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    salary = models.IntegerField()
    image = models.ImageField(upload_to="image", default='test.png')

    def __str__(self):
        return f"{self.name}{self.email}{self.salary}{self.image}"