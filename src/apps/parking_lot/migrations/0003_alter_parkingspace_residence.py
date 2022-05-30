# Generated by Django 4.0.4 on 2022-05-30 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0010_alter_block_name_alter_residence_unique_together_and_more'),
        ('parking_lot', '0002_alter_parkingspace_parking_space_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='residence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='residential.residence', verbose_name='Residencia'),
        ),
    ]
