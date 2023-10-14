from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def login(request):
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
                    
                    # authenticate.login(request,user)
                    # messages.success(request,'you are sucessfully login ')
                    # return redirect('dashboard')
                    user.save()
                    messages.success(request,'account haas been created successfully')
        else:
            messages.error(request,'Sorry password not match')
            return redirect('signup')
    else:   
        return render(request,'account/signup.html')
    return render(request,'account/signup.html')

def logout(request):
    return logout('home')

def dashboard(request):
    return render(request,'account/dashboard.html')