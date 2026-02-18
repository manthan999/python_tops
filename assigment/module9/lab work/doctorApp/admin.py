from django.contrib import admin
from doctorApp.models import *
# Register your models here.

class displayDoctor(admin.ModelAdmin):
    list_display = ["id", "docName", "docSpecialization", "docHospital", "docExperience"]

admin.site.register(Doctor, displayDoctor)