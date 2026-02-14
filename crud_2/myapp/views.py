from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    return render (request,"index.html")

def register(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")
        if id:
            st = Student.objects.get(pk=id)
            st.name=name
            st.email=email
            st.phone=phone
            st.age=age
            st.save()
            return render (request,"index.html",{"done":"successfully"})
        else:
            Student.objects.create(name=name,email=email,phone=phone,age=age)
            return render (request,"index.html",{"msg":"Registration successfully !!!"})

def display(request):
    students = Student.objects.all()
    return render (request,"display.html",{"students":students})

def delete_student(request):
    did = request.GET["did"]
    st = Student.objects.get(pk=did)
    st.delete()
    return redirect("display")

def update_student(request):
    uid = request.GET["uid"]
    st = Student.objects.get(pk=uid)
    return render (request,"index.html",{"st":st})