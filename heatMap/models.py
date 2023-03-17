from django.db import models

from .bd.pythonSQL import catchAllbyID
# Create your models here.


class Coordenadas(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

    def __str__(self) -> int:
        return (self.id, [self.latitude, self.longitude]) # Retorna o id e as coordenadas, ao invés do objeto

    class Meta:
        managed = False
        db_table = 'coordenadas'

class Meses(models.Model):
    id = models.OneToOneField(Coordenadas, models.DO_NOTHING, db_column='id', primary_key=True)
    janeiro21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fevereiro21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    marco21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    abril21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    maio21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    junho21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    julho21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    agosto21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    setembro21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    outubro21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    novembro21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    dezembro21 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    janeiro22 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self) -> int:
        return self.id.id # Retornando o id e a intensidade dos meses, ao invés do objeto

    class Meta:
        managed = False
        db_table = 'meses'