from django.db import models

# Create your models here.


class Block(models.Model):
    name = models.CharField(verbose_name='Nombre del bloque', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'

    def __str__(self):
        return self.name


class Residence(models.Model):
    RESIDENCE_TYPE = (
        ('apartment', 'Apartamento'),
        ('house', 'Casa'),
    )
    residence_type = models.CharField(verbose_name='Tipo de residencia', max_length=30, choices=RESIDENCE_TYPE)
    block = models.ForeignKey(Block, verbose_name='Bloque', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name='Número de residencia')
    phone = models.CharField(verbose_name='Teléfono', max_length=20, blank=True, null=True)
    busy = models.BooleanField(verbose_name='¿Está ocupada?', default=True)

    class Meta:
        unique_together = ('block', 'number')
        verbose_name = 'Residencia'
        verbose_name_plural = 'Residencias'

    def get_residence_type(self):
        return dict(self.RESIDENCE_TYPE)[self.residence_type]

    def __str__(self):
        return f'{self.get_residence_type()} - {self.block} {self.number}'

