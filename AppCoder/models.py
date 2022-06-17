from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField("Nombre", max_length=20)
    apellido = models.CharField("Apellido", max_length=20)
    edad = models.IntegerField("Edad")
    fecha = models.DateField("Fecha")
