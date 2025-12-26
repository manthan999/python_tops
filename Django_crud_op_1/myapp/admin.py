from django.contrib import admin
from myapp.models import *
# Register your models here.

class productDisplay(admin.ModelAdmin):
    list_display = ['name','weight','price']

admin.site.register(product,productDisplay) 