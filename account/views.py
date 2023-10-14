from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'account/login.html')

def signup(request):
    return render(request,'account/signup.html')

def logout(request):
    return logout('home')

def dashboard(request):
    return render(request,'account/dashboard.html')