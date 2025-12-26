from django.contrib import admin
from crudapp.models import *

# Register your models here.

class studentdisplay(admin.ModelAdmin):
        list_display = ["name","email","phone","age"]

admin.site.register(Student,studentdisplay)