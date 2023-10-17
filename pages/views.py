from django.shortcuts import render,HttpResponse,redirect
from .models import Team,Contact
from cars.models import Car
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
def home(request):
    # return HttpResponse("loremIpsm")
    team_ret=Team.objects.all() #decleraing for calling function from our database
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')
    model_fields=Car.objects.values_list('model',flat=True).distinct() #this will give individual data from the database no repeating adn return the value in list
    location_fields=Car.objects.values_list('city',flat=True).distinct()
    build_year=Car.objects.values_list('year',flat=True).distinct()
    body_fields=Car.objects.values_list('body_style',flat=True).distinct()
    transmission=Car.objects.values_list('transmission',flat=True).distinct()

    
    
    data={
        'team':team_ret,
        'ft_car':featured_car,
        'All_car':all_car,
        'model_fields':model_fields,
        'location_fields':location_fields,
        'build_fields':  build_year,
        'body_fields': body_fields,
        'transmission':transmission
    }
    return render(request,'pages/home.html',data)
def about(request):
    team_retn=Team.objects.all()
    data={
        'team':team_retn,
    }
    return render(request,'pages/about.html',data)
def services(request):
    return render(request,'pages/services.html')
def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']
        
        contact_form=Contact(name=name,email=email,subject=subject,message=message,phone=phone)
        contact_form.save()
        
    #     email_subject="You have new mail regarding this " + subject
    #     message_body="Name" + name + ".Email" + email + ".phone" + phone + ".messages" + message
    #     admin_detail=User.objects.get(is_superuser=True)
    #     admin_email=admin_detail.email
    #     send_mail(
    #             email_subject,
    #             message_body,
    #             'bida_csit2077@lict.edu.np',
    #             [admin_email],
    #             fail_silently=False,
    # )
    # #     try:
    # #         admin_detail = User.objects.get(is_superuser=True)
    # #         admin_email = admin_detail.email
    # #         send_mail(
    # #             'New Car Inquiry',
    # #             'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.',
    # #             'bida_csit2077@lict.edu.np',
    # #             [admin_email],
    # #             fail_silently=False,
    # #         )
    # #     except ObjectDoesNotExist:
    # #                 messages.error(request, 'No superuser found to handle the inquiry.')
    # #     except MultipleObjectsReturned:
    # # # Handle the case when there are multiple superusers (e.g., send the email to all superusers)
    # #             superusers = User.objects.filter(is_superuser=True)
    # #     for superuser in superusers:
        
        
        messages.success(request,'We will contact you soon!')
        return redirect('contact')
    return render(request,'pages/contact.html')