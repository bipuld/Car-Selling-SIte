from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.cars, name='cars'),    
    path('car_details/<int:id>/', views.car_details, name='car_details'),
]

