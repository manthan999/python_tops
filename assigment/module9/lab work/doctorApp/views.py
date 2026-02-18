from django.shortcuts import render, redirect
from doctorApp.models import *
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

# Create your views here.
def indexPage(request):
    return render(request, "index.html")

def registerPage(request):
    return render(request, "register.html")

def loginPage(request):
    return render(request, "login.html")

def doctorInfoPage(request):
    data = Doctor.objects.all()
    is_Staff = request.user.groups.filter(name__in=["Staff", "Admins"]).exists()
    return render(request, "doctorInfo.html", {"data": data, "is_Staff": is_Staff})

@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name="Staff").exists())
def doctorFormPage(request):
    return render(request, "doctorForm.html")

# helper function
def is_Staff_Admin(user):
    return user.is_superuser or user.groups.filter(name="Staff").exists()

# Api urls:

@login_required(login_url="login")
@user_passes_test(is_Staff_Admin)
def addDoctor(request):
    data = request.POST
    docName = data.get("docName")
    docSpecialization = data.get("docSpecialization")
    docHospital = data.get("docHospital")
    docExperience = data.get("docExperience")

    dobj = Doctor(
        docName= docName,
        docSpecialization= docSpecialization,
        docHospital= docHospital,
        docExperience= docExperience
    )
    dobj.save()
    print(docName)
    return JsonResponse({"status":201, "message": "Doctor Successfully Added"})

@user_passes_test(is_Staff_Admin)
def editRedirect(request):
    docId = request.GET["id"]
    dobj = Doctor.objects.get(id=docId)
    return render(request, "doctorForm.html", {"docInfo": dobj})

@user_passes_test(is_Staff_Admin)
def updateDoctor(request):
    data = request.POST
    docId = data.get("docId")
    docName = data.get("docName")
    docSpecialization = data.get("docSpecialization")
    docHospital = data.get("docHospital")
    docExperience = data.get("docExperience")

    print(docId, docName, docSpecialization, docHospital, docExperience)
    dobj = Doctor.objects.get(id = docId)
    dobj.docName = docName
    dobj.docSpecialization = docSpecialization
    dobj.docHospital = docHospital
    dobj.docExperience = docExperience
    dobj.save()

    return JsonResponse({"status":201, "message": "Doctor Updated Successfully!"})

@user_passes_test(is_Staff_Admin)
def deleteDoctor(request):
    docId = request.GET["id"]
    dobj = Doctor.objects.get(id=docId)
    dobj.delete()
    return redirect(doctorInfoPage)


def registerUser(request):
    data = request.POST
    userName = data["userName"]
    userEmail = data["userEmail"]
    userPassword = data["userPassword"]

    uobj = User(
        username = userName,
        email = userEmail
    )
    uobj.set_password(userPassword)
    uobj.save()
    usergroup = Group.objects.get(name="generalUser")
    uobj.groups.add(usergroup)

    now = datetime.now()
    formatted_datetime = now.strftime("%A, %B %d, %Y at %I:%M %p")

    send_mail(
        "DocFinder - Account Created!", 
        f"DocFinder \nHello {userName}! Your Account on DocFinder has been successfully created with email address ({userEmail}) at {formatted_datetime}", 
        settings.EMAIL_HOST_USER, 
        [userEmail]
    )
    return JsonResponse({"status":"success", "message":"Account Created!"})

def loginUser(request):
    data = request.POST
    userName = data["userName"]
    userPassword = data["userPassword"]

    print(userName,userPassword)
    user = authenticate(username=userName, password=userPassword)
    print("user found: ",user)
    if user is not None:
        login(request, user)
        return JsonResponse({"status":"success", "message":"Login Successful!"})
    else: 
        return JsonResponse({"status": "failed", "message":"Authentication Failed!"})

def logoutUser(request):
    logout(request)
    return render(request, "index.html")    


