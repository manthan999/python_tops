from django.urls import path 
from ajax.views import *

urlpatterns = [
    path ("",index,name="index"),
    path ("register",register,name="register"),

    path("countries",countries,name="countries"),
    path("states",states,name="states"),
    path("cities",cities,name="cities"),
]