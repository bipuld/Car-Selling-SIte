# Generated by Django 4.1.3 on 2023-01-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_id',
            field=models.IntegerField(default=True),
        ),
    ]
