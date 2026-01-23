from django.shortcuts import render
import razorpay
from django.http import HttpResponse,JsonResponse 
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request,"index.html")

def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    print(payment)
    return JsonResponse(payment)

def sendmail(request):
    try :
        send_mail("testing","testing",settings.EMAIL_HOST_USER,["manthanpuniwala@gmail.com"])
        print("email send successfully")
    except Exception as e :
        print(e)
    pass