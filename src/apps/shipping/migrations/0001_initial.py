# Generated by Django 4.0.4 on 2022-05-30 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residential', '0006_delete_shipping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=900, null=True, verbose_name='Descripción de la multa')),
                ('details', models.CharField(blank=True, max_length=900, null=True, verbose_name='Descripción de la multa')),
                ('reception_date', models.DateTimeField(verbose_name='Fecha de recepción')),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.residence', verbose_name='Residencia')),
            ],
            options={
                'verbose_name': 'Envío',
                'verbose_name_plural': 'Envíos',
            },
        ),
    ]
