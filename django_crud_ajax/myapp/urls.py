from django.urls import path 
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("addstudent",addstudent,name="addstudent"),
    path("display",display,name="display"),
    path("delete",delete_student,name="delete"),
    path("getbtid",getbyid,name="getbyid"),
    path("updatestudent",updatestudent,name="updatestudent")
]