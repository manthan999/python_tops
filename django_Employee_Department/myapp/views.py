from django.shortcuts import render, redirect
from myapp.models import Department, Employee

def index(request):
    departments = Department.objects.all()
    return render(request, "index.html", {"departments": departments})


def register(request):
    if request.method == 'POST':
        data = request.POST

        department_id = data.get("department")
        name = data.get("name")
        email = data.get("email")
        salary = data.get("salary")
        image = request.FILES.get("image")

        department = Department.objects.get(id=department_id)

        Employee.objects.create(
            department=department,
            name=name,
            email=email,
            salary=salary,
            image=image,
        )

    return redirect("display")  



def display(request):
    employees = Employee.objects.all()
    return render(request, "display.html", {"employees": employees})
