from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from myapp.models import *
# Create your views here.


def index (request):
    return render (request,"index.html")

def addstudent(request):
    if request.method=="POST":
        name = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']


    student.objects.create(name=name,email=email,phone=phone)
    return HttpResponse("student added !!!")

def display(request):
    students = student.objects.all()
    return JsonResponse({"students":list(students.values())})

def delete_student(request):
    sid = request.GET['sid']
    students = student.objects.get(pk=sid)
    students.delete()
    return HttpResponse("student deleteed !!!")

def getbyid (request):
    sid = request.GET['sid']
    students = student.objects.filter(id=sid)
    return JsonResponse({"students":list(students.values())})
    
def updatestudent(request):
    if request.method=="POST":
        id = request.POST["id"]
        name = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']

        students = student.objects.get(pk=id)
        students.name = name 
        students.email = email
        students.phone = phone
        students.save()

        return HttpResponse("student updated !!!")