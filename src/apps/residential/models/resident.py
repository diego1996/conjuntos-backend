from django.db import models

# Create your models here.
from src.apps.residential.models.residence import Residence


class Resident(models.Model):
    RESIDENT_TYPE = (
        ('tenant', 'Arrendatario'),
        ('habitant', 'Habitante'),
        ('owner', 'Propietario'),
    )
    residence = models.ForeignKey(Residence, verbose_name='Residencia', on_delete=models.CASCADE)
    resident_type = models.CharField(verbose_name='Tipo de residente', max_length=30, choices=RESIDENT_TYPE)
    first_name = models.CharField(verbose_name='Nombres', max_length=250)
    last_name = models.CharField(verbose_name='Apellidos', max_length=250)
    cellphone = models.CharField(verbose_name='Celular', max_length=20, blank=True, null=True)
    whatsapp = models.CharField(verbose_name='WhatsApp', max_length=20, blank=True, null=True)
    active = models.BooleanField(verbose_name='¿Está activo/a?')

    class Meta:
        unique_together = ('residence', 'resident_type', 'first_name', 'last_name')
        verbose_name = 'Residente'
        verbose_name_plural = 'Residentes'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.cellphone}'

