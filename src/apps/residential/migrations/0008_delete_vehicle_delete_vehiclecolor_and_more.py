# Generated by Django 4.0.4 on 2022-05-30 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0002_alter_parkingspace_parking_space_type'),
        ('residential', '0007_remove_vehicle_residence_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.DeleteModel(
            name='VehicleColor',
        ),
        migrations.DeleteModel(
            name='VehicleType',
        ),
    ]
