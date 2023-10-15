from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.


class Inquire(models.Model):
    car_id=models.IntegerField()
    user_id=models.IntegerField()
    car_title=models.CharField(max_length=200)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    customer_need=models.CharField(max_length=250)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    message=RichTextField() 
    create_date=models.DateTimeField(blank=False,default=datetime.now)
    
    def __str__(self):
        return self.email