from django.db import models

# Create your models here.
class Tienda(models.Model):
    categoria = models.TextField()
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.TextField()
    stock = models.IntegerField()
