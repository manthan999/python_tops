from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("home",home,name="home"),
    path("user_logout",user_logout,name="user_logout"),
]