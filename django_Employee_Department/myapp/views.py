from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    Departments = Department.objects.all()

    return render(request,"index.html",{"Departments":Departments})

def register(request):
    if request.method=='POST':
        data = request.POST
        Department= data.get("Department")
        name = data.get("name")
        email= data.get("email")
        salary= data.get("salary")
        file = request.FILES['file']

        Product.objects.create(
            Department= Department.objects.get(pk=Department),
            name = name,
            email=email,
            salary=salary,
            image = file
        )
        
        return redirect("index")

def display(request):
    Employeeloyee = Employee.objects.all()
    return render(request,'display.html',{"Employee":Employee})
    