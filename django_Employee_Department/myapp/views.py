from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    department = Department.objects.all()
    return render(request,"index.html",{"departments":department})

def register(request):
    if request.method=='POST':
        data = request.POST
        department= data.get("department")
        id = data.get('id')
        name = data.get("name")
        email= data.get("email")
        salary= data.get("salary")
        file = request.FILES['file']

        if not id:

            Employee.objects.create(
                department= Department.objects.get(pk=Department),
                name = name,
                email=email,
                salary=salary,
                image = file
                )
    return render(request,'index.html')

def display(request):
    employees = Employee.objects.all()
    return render(request,'display.html',{"employees":employees})