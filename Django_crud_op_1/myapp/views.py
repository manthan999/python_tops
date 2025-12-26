from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
     if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        weight = data.get("weight")
        price = data.get("price")
        if id :
            p  = product.objects.get(pk=id)
            p.name = name
            p.weight = weight
            p.price = price
            p.save()
            return render(request,'index.html',{"done":"Update successfully !!!"})

        else :
           
            product.objects.create(name=name,weight=weight,price=price)
            return render(request,'index.html',{"msg":"Registration successfully !!!"})


def display(request):
    products = product.objects.all()
    return render(request,"display.html",{"products":products})
    
def delete_product(request):
    did = request.GET['did']
    p = product.objects.get(pk=did)
    p.delete()
    return redirect("display")
    
def update_product(request):
    uid = request.GET['uid']
    p = product.objects.get(pk=uid)
    return render(request,"index.html",{"p":p})
