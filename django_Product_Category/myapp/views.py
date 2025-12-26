from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()

    return render(request,"index.html",{"categories":categories})

def register(request):
    if request.method=='POST':
        data = request.POST
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        file = request.FILES['file']

        Product.objects.create(
            category = Category.objects.get(pk=category),
            name = name,
            price=price,
            qty=qty,
            image = file
        )
        
        return redirect("index")
    

def display(request):
    products = Product.objects.all()
    return render(request,'display.html',{"products":products})