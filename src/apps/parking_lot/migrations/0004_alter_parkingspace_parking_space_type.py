# Generated by Django 4.0.4 on 2022-05-30 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicle_license_plate'),
        ('parking_lot', '0003_alter_parkingspace_residence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='parking_space_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicletype', verbose_name='Tipo de espacio/vehiculo'),
        ),
    ]
