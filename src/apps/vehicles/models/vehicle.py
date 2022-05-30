from django.db import models

# Create your models here.
from src.apps.residential.models import Residence


class VehicleType(models.Model):
    name = models.CharField(verbose_name='Nombre del tipo de vehiculo', max_length=250)

    class Meta:
        verbose_name = 'Tipo de vehiculo'
        verbose_name_plural = 'Tipos de vehiculos'

    def __str__(self):
        return self.name


class VehicleColor(models.Model):
    name = models.CharField(verbose_name='Nombre del color del vehiculo', max_length=250)

    class Meta:
        verbose_name = 'Color de vehiculo'
        verbose_name_plural = 'Colores de vehiculos'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    residence = models.ForeignKey(Residence, verbose_name='Residencia', on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, verbose_name='Tipo de vehiculo', on_delete=models.CASCADE)
    vehicle_color = models.ForeignKey(VehicleColor, verbose_name='Color del vehiculo', on_delete=models.CASCADE)
    license_plate = models.CharField(verbose_name='Placa del vehiculo', unique=True, max_length=250)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return f'{self.vehicle_type} - {self.vehicle_color}'

