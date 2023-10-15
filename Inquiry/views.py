from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Inquire

# Create your views here.
def inquiry(request):
    if request.method == "POST":
        car_id=request.POST['car_id']
        user_id=request.POST['user_id']
        car_title=request.POST['car_title']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        print(request.POST)
        contact= Inquire(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)
        contact.save()
        
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Inquire.objects.filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'We have already received your Inquiry we will get in  touch  with you soon')
                return redirect('/car_details/'+car_id)
        messages.success(request,'Your request has been submitted, we will get back to you shortly.')
        return redirect('/car_details/'+car_id)