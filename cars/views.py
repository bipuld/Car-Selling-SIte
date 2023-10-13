from django.shortcuts import render,get_object_or_404,HttpResponse
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


def search(request):
    car=Car.objects.order_by('-created_date').all()
    
    
    
    
    # this is for the search fields
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            car=car.filter(description__icontains=keyword)
            
            
    #this is for the model match fields
    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            car=car.filter(model__iexact=model) #this match the exact model with the car in database

    if 'location' in  request.GET:
        location=request.GET['location']
        if location:
            car=car.filter(city__iexact=location)
            

    if 'year' in  request.GET:
        year=request.GET['year']
        if year:
            car=car.filter(year__iexact=year)
                    
    if 'body_type' in  request.GET:
        style=request.GET['body_type']
        if style:
            car=car.filter(body_style__iexact=style)
                           
    if 'transmission' in  request.GET:
        transmission=request.GET['transmission']
        if transmission:
            car=car.filter(transmission__iexact=transmission)
    
    if 'min_price' in request.GET:
        minPrice=request.GET["min_price"]
        maxprice=request.GET['max_price']
        if maxprice:
            car=car.filter(price__gte=minPrice,price__lte=maxprice)
                  
    context={
        'cars':car
        
    }
    return render(request,'cars/search.html',context)