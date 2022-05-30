from django.db import models

# Create your models here.
from src.apps.residential.models import Residence
from src.apps.vehicles.models.vehicle import VehicleType


class ParkingZone(models.Model):
    name = models.CharField(verbose_name='Nombre de la zona de parqueo', max_length=250)

    class Meta:
        verbose_name = 'Zona de parqueo'
        verbose_name_plural = 'Zonas de parqueo'

    def __str__(self):
        return self.name


class ParkingSpace(models.Model):
    residence = models.ForeignKey(Residence, verbose_name='Residencia', blank=True, null=True, on_delete=models.CASCADE)
    parking_zone = models.ForeignKey(ParkingZone, verbose_name='Zona del espacio de parqueo', on_delete=models.CASCADE)
    number = models.CharField(verbose_name='Número del espacio de parqueo', max_length=250)
    parking_space_type = models.ForeignKey(VehicleType, verbose_name='Tipo de espacio/vehiculo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Espacio de parqueo'
        verbose_name_plural = 'Espacios de parqueo'

    def __str__(self):
        return f'{self.parking_zone} - {self.number}'
