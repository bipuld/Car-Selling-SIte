from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from Inquiry.models import Inquire
from cars.models import Car
# Create your views here.

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(request.POST)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully log in ") 
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credential")
            return redirect('login')
            
    return render(request,'account/login.html')
def signup(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        print(request.POST) 
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'user already exist')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,'account has been created successfully')
        else:
            messages.error(request,'Sorry password not match')
            return redirect('signup')
    else:   
        return render(request,'account/signup.html')
    return render(request,'account/signup.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"You are now logout !!")
        return redirect('home')
    
@login_required(login_url="login")
def dashboard(request):
    user_inquiry=Inquire.objects.order_by('-create_date').filter(user_id=request.user.id)   
    data={
        'inquires':user_inquiry,
    }
    return render(request,'account/dashboard.html',data)