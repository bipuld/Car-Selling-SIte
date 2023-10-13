from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# from multiselectfield import MultiSelectField
# Create your models here.
class Car(models.Model):
    st_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    fuel_choices=(('diesel', 'diesel'),
               ('petrol', 'petrol'),
               ('hybrid', 'hybrid'))
    year_choices=[]
    for r in range (1990,(datetime.now().year+1)):
        year_choices.append((r,r))
    id=models.IntegerField(primary_key=True,default=True)    
    car_title = models.CharField(max_length=200)
    state= models.CharField(choices=st_choices, max_length=100)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=20)
    year = models.IntegerField(('year'), choices=year_choices)
    condition = models.CharField(max_length=200)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    features = MultiSelectField(choices=features_choices,max_length=200)
    body_style = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    interior= models.CharField(max_length=200)
    miles= models.IntegerField()
    doors = models.CharField(choices=door_choices,max_length=10)
    passengers= models.IntegerField()
    vin_num = models.CharField(max_length=200)
    milage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choices,max_length=50,default=True)
    no_of_owner = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date= models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.car_title
        