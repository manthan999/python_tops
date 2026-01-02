from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
import os
def index(request):
    categories = Category.objects.all()

    return render(request,"index.html",{"categories":categories})

def register(request):
    if request.method=='POST':
        data = request.POST
        id = data.get('id')
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
       

        if id : 
           prod = Product.objects.get(pk=id)
           prod.category = Category.objects.get(pk=category)
           prod.name = name
           prod.price=price
           prod.qty=qty
           if request.FILES:
             if prod.image != "default.png":
                os.remove(f"media/{prod.image}")
             prod.image = request.FILES['file']
             
           prod.save()
        else :

            if  request.FILES:
                file = request.FILES['file']
            else:
                file = "default.png"
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

def delete_product(request):
    id = request.GET['id']
    prod = Product.objects.get(pk=id)
    print(prod.image)
    if prod.image != "default.png":
        os.remove(f"media/{prod.image}")
    prod.delete()
    return redirect("display")

def product_by_id(request):
    categories = Category.objects.all()
    id = request.GET['id']
    prod = Product.objects.get(pk=id)
    return render(request,"index.html",{"prod":prod,"categories":categories})