from django.contrib import admin
from myapp.models import *
# Register your models here.

# class Categorydisply(admin.ModelAdmin):
#     list_display = ('name')

# class Productdisply(admin.ModelAdmin):
#     list_display = ('name','price','qty','image')

admin.site.register(Category)
admin.site.register(Product)