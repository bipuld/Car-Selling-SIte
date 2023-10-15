from django.contrib import admin
from .models import Inquire
# Register your models here.


@admin.register(Inquire)
class Inquire(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25
