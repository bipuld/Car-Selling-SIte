from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation= models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    facebook_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    linkdein_link = models.URLField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
     return self.first_name

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    phone=models.CharField(max_length=50)    
    message=RichTextField()
    contact_date=models.DateTimeField(default=datetime.now())
    def __str__(self):
       return self.name