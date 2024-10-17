from django.db import models

# Create your models here.
class Pet (models.Model):
    nome = models.CharField(max_length = 15)
    idade =  models.DecimalField(max_digits = 5, decimal_places = 2)
    data_nascimento = models.DateField()
    raca = models.CharField(max_length = 15)
    cor = models.CharField(max_length = 15)
    peso = models.DecimalField(max_digits = 5, decimal_places = 2)
    