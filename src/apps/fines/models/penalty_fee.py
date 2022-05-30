from django.db import models

# Create your models here.
from djmoney.models.fields import MoneyField

from src.apps.residential.models import Residence


class PenaltyFeeType(models.Model):
    name = models.CharField(verbose_name='Nombre del tipo de multa', max_length=250)

    class Meta:
        verbose_name = 'Tipo de multa'
        verbose_name_plural = 'Tipos de multas'

    def __str__(self):
        return self.name


class PenaltyFee(models.Model):
    residence = models.ForeignKey(Residence, verbose_name='Residencia', on_delete=models.CASCADE)
    penalty_fee_type = models.ForeignKey(PenaltyFeeType, verbose_name='Tipo de multa', on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Descripción de la multa', max_length=900)
    penalty_fee_date = models.DateTimeField(verbose_name='Fecha de la multa')
    amount_to_paid = MoneyField(verbose_name='Monto a pagar', max_digits=14, decimal_places=2, default_currency='COP',
                                default=0)
    active = models.BooleanField(verbose_name='¿Está activa?')

    class Meta:
        verbose_name = 'Multa'
        verbose_name_plural = 'Multas'

    def __str__(self):
        active_text = 'Pendiente' if self.active else 'Solucionada'
        return f'{self.penalty_fee_type} - {self.penalty_fee_date} - {active_text}'
