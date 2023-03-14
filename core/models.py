from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100) # Máximo de 100 caracteres

    def __str__(self) -> str:
        return self.nome # Retornando o nome da pessoa, ao invés do objeto