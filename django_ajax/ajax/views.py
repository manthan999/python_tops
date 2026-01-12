from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from ajax.models import *
# Create your views here.

def index(request):
    return  render (request,"index.html")

def register(request):
    data = request.GET['data']
    products = product.objects.filter(name__startswith=data)
    return JsonResponse ({"products":list(products.values())})

def countries(request):
    countries = country.objects.all()
    return JsonResponse({"countries":list(countries.values())})

def states(request):
    cid = request.GET['cid']
    states = state.objects.filter(country_id=cid)
    return JsonResponse({"states":list(states.values())})

def cities(request):
    sid = request.GET['sid']
    cities = city.objects.filter(state_id=sid)
    return JsonResponse({"cities":list(cities.values())})

