from django.contrib import admin
from myapp.models import *
# Register your models here.

class studentdata(admin.ModelAdmin):
     list_display = ["name","email","phone","age"]

class employeedata(admin.ModelAdmin):
     list_display = ["name","email","phone","age","salary"]

admin.site.register(student,studentdata)
admin.site.register(employee,employeedata)
