from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serialiozer import *
# Create your views here.

@api_view(['GET'])
def get_api(request):
    return Response({"meg":"GET API CALL"}) 

@api_view(['POST'])
def post_api(request):
    return Response({"meg":"POST API CALL"}) 

@api_view(['PUT'])
def put_api(request):
    return Response({"meg":"PUT API CALL"}) 

@api_view(['DELETE'])
def delete_api(request):
    return Response({"meg":"DELETE API CALL"}) 

@api_view(['GET'])
def students(request):
    students = Student.objects.all()
    ser=Studentserializers(students,many=True)
    return Response({"data":ser.data})
    
@api_view(['POST'])
def add_students(request):
    ser = Studentserializers(data=request.data)
    if not ser.is_valid():
        return Response({"errors":ser.error,"mes":"........"})
    else:
        ser.save()
        return Response({"data":ser.data,"meg":"ADD"})
    

@api_view(['PUT'])
def update_students(request,id):
    std = Student.objects.get(pk=5)
    ser = Studentserializers(std,request.data,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"mes":"........"})
    else:
        ser.save()
        return Response({"data":ser.data,"meg":"ADD"})
    
@api_view(['DELETE'])
def delete_students(request,id):
    std = Student.objects.get(pk=5)
    std.delete()
    return Response({"meg":"delete"})