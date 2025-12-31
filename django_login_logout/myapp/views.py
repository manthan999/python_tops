from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get('uname')
        password = data.get('password')

        user = authenticate(username=uname,password=password)
        if user is not None :
            login(request,user)
            return render(request,"home.html")
        else:
            return render(request,"index.html",{"err":"Invalid credentials"})
        
    if request.user.is_authenticated:
        return render(request,"home.html")

    return render(request,"index.html")


def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        uname = data.get('uname')
        password = data.get('password')

        u = User(first_name=fname,last_name=lname,username=uname)
        u.set_password(password)
        u.save()
        return render(request,"reg.html",{"msg":"Registration successful"})


    return render (request,"reg.html")

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return render(request,"index.html")
