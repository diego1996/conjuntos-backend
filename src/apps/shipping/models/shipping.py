from django.db import models

# Create your models here.
from src.apps.residential.models import Residence


class Shipping(models.Model):
    residence = models.ForeignKey(Residence, verbose_name='Residencia', on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Descripción del envío', blank=True, null=True, max_length=900)
    details = models.CharField(verbose_name='Detalles del envío', blank=True, null=True, max_length=900)
    reception_date = models.DateTimeField(verbose_name='Fecha de recepción')

    class Meta:
        verbose_name = 'Envío'
        verbose_name_plural = 'Envíos'

    def __str__(self):
        return f'{self.residence} - {self.description}'

