from django.shortcuts import render
import razorpay
from .models import * 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
@api_view(['POST'])
def home(request):
    if request.method=='POST':
        name = request.data['name']
        amount = request.data['amount']
        email= request.data['email']
        client = razorpay.Client(auth=("rzp_test_X7XVZBmzec6QDz", "D837xj4m3EAXUHJqRGaRR5jM"))
        payment=payment = client.order.create({"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
        coffee=Coffee(name=name,amount=amount,email=email,payment_id=payment['id'])
        coffee.save()
        return render(request,"index.html",{'payment':payment})
        #    print(name)
        #  print(int_amount)
    return render(request, "index.html")


  

@csrf_exempt
def success(request):
    if request.method=='POST':
         a=request.POST
         order_id=""
         for key , val in a.items:
             if key=='razorpay_order_id':
                order_id=val
                break
         user=Coffee.objects.filter(order_id=order_id).first()
         user.paid=True
         user.save()
         msg_plain=render_to_string('email.txt')
         msg_html=render_to_string('email.html')  
         send_mail("Your Donation has been recived",msg_plain,settings.EMAIL_HOST_USER,[user.email],html_message=msg_html)
           
        #  print(a)
    return render(request,"success.html")
