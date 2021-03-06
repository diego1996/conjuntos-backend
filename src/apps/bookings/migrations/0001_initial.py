# Generated by Django 4.0.4 on 2022-05-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residential', '0005_delete_booking_delete_bookingspace'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del espacio que se puede reservar')),
            ],
            options={
                'verbose_name': 'Espacio de reserva',
                'verbose_name_plural': 'Espacios de reserva',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio de la reserva')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de fin de la reserva')),
                ('booking_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.bookingspace', verbose_name='Espacio que reserva')),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.residence', verbose_name='Residencia')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]
