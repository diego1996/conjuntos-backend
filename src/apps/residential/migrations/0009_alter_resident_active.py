# Generated by Django 4.0.4 on 2022-05-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0008_delete_vehicle_delete_vehiclecolor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='active',
            field=models.BooleanField(verbose_name='¿Está activo/a?'),
        ),
    ]
