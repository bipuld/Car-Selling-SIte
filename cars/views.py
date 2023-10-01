from django.shortcuts import render,get_object_or_404
from cars.models import Car
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.urls import reverse
# Create your views here.p
def cars(request):
    # car=Car.objects.order_by('-created_date'),
    car=Car.objects.order_by('-created_date').all()
    context={
        'cars': car
    }
    return render (request,'cars/cars.html',context)

def car_details(request, id):
    single_car = get_object_or_404(Car, id=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_details.html', data)
