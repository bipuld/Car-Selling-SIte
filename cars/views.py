from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from cars.models import Car




def cars(request):
    car=Car.objects.order_by('-created_date').all()
    
    
    paginator=Paginator(car,3)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    
    
    context={
        'cars': paged_cars
    }
    return render (request,'cars/cars.html',context)

def car_details(request, id):
    single_car = get_object_or_404(Car, id=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_details.html', data)
