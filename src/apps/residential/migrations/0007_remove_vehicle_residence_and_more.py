# Generated by Django 4.0.4 on 2022-05-30 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0006_delete_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_color',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_type',
        ),
    ]
