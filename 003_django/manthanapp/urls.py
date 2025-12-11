from django.urls import *
from manthanapp.views import *


urlpatterns=[
    path("",hm,name="hm"),
    path("meet",meet,name="meet"),
    path("krish",krish, name="krish"),
    path("chintan",chintan,name="chintan"),
]
