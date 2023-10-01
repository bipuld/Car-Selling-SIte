from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html('<img src="{}" width ="40" style = " border-radius: 50px;"/>'.format(obj.photo.url)) #by using image tag for dispalying image in admin page
    thumbnail.short_description = 'photo'
    list_filter=('designation' ,)
    list_display=('id','thumbnail','first_name', 'last_name', 'created_date',)
    list_display_links=('id', 'first_name',)
    search_fields=('id', 'first_name')
admin.site.register(Team,TeamAdmin)
#this is the for changing heading of database part of our admin site
admin.site.site_header = "Admin Team"
admin.site.index_title = "Welcome to Car B&S"
admin.site.site_title = "project tutorial"  

