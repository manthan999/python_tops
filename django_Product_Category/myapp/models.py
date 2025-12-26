from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image", default='test.png')

    def __str__(self):
        return f"{self.name}{self.price}{self.qty}{self.image}"