from django.urls import *
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("blog",blog,name="blog"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("contact",contact,name="contact"),
    path("services",services,name="services"),
    path("shop",shop,name="shop"),
    path("thankyou",thankyou,name="thankyou"),
]
