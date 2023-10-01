from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html('<img src="{}" width="40" style="border-radius :50px;"/>'.format(obj.car_photo.url))
    thumbnail.short_description = 'car_photo'
    list_display=('id','thumbnail',"car_title",'city','color',"model",'year','body_style','fuel_type','is_featured')
    list_display_links=("car_title",'model')
    search_fields=('id','car_title','model','city','body_style','fuel_type')
    list_editable=('is_featured',)
    list_filter=('model','city','body_style','fuel_type')
admin.site.register(Car,CarAdmin)
