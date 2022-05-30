from django.db import models


# Create your models here.
from src.apps.residential.models import Residence


class BookingSpace(models.Model):
    name = models.CharField(verbose_name='Nombre del espacio que se puede reservar', max_length=250)

    class Meta:
        verbose_name = 'Espacio de reserva'
        verbose_name_plural = 'Espacios de reserva'

    def __str__(self):
        return self.name


class Booking(models.Model):
    residence = models.ForeignKey(Residence, verbose_name='Residencia', on_delete=models.CASCADE)
    booking_space = models.ForeignKey(BookingSpace, verbose_name='Espacio que reserva', on_delete=models.CASCADE)
    start_date = models.DateTimeField(verbose_name='Fecha de inicio de la reserva')
    end_date = models.DateTimeField(verbose_name='Fecha de fin de la reserva')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'{self.booking_space} - {self.start_date} - {self.end_date}'

