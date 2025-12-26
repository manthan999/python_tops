from django.contrib import admin
from myapp.models import *
# Register your models here.

# class Departmentdisply(admin.ModelAdmin):
#     list_display = ('name')

# class Employeedisply(admin.ModelAdmin):
#     list_display = ('name','email','salary')

admin.site.register(Department)
admin.site.register(Employee)