from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()

    return render(request,"index.html",{"categories":categories})

def register(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        file = request.FILES['file']

        if not id:

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

def delete(request):
    id = request.GET['id']
    prod = Product.objects.get(pk=id)
    print(prod.image)
    prod.delete()
    return redirect("display")

def edit(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        file = request.FILES['file']

        if id:
            prod=Product.objects.get(pk=id)
        else:
            prod=Product()
        prod.category=category
        prod.name=name
        prod.price=price 
        prod.qty=qty 
        if file:
            prod.file=file 
        prod.save()
        return render(request,'index.html',{'msg':'update successfully..'})
    else:
        id=request.GET.get('id')
        if id:
            prod=Product.objects.get(pk=id)
            return render(request,'index.html',{'prod':prod})
        return render(request,'index.html')