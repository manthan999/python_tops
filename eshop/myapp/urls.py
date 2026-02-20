from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
from myapp.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)
router.register("carts",CartViewSet,basename="carts"),
router.register("address",AddressViewSet,basename="address")

urlpatterns = [
    path('', include(router.urls)),


]