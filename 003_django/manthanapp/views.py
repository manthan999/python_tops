from django.shortcuts import render

# Create your views here.

def hm(request):
    return render(request,"hm.html") 

def meet(request):
    return render(request,"meet.html") 

def krish(request):
    return render(request,"krish.html") 

def chintan(request):
    return render(request,"chintan.html") 