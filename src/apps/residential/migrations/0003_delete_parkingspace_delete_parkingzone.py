# Generated by Django 4.0.4 on 2022-05-30 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0002_alter_vehicle_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParkingSpace',
        ),
        migrations.DeleteModel(
            name='ParkingZone',
        ),
    ]
