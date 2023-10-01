from django.shortcuts import render,HttpResponse
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    # return HttpResponse("loremIpsm")
    team_ret=Team.objects.all() #decleraing for calling function from our database
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')
    data={
        'team':team_ret,
        'ft_car':featured_car,
        'All_car':all_car,
    }
    return render(request,'pages/home.html',data)
def about(request):
    team_retn=Team.objects.all() #decleraing for calling function from our database
    data={
        'team':team_retn,
    }
    return render(request,'pages/about.html',data)
def services(request):
    return render(request,'pages/services.html')
def contact(request):
    return render(request,'pages/contact.html')