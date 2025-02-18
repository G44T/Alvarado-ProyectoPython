from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)
    precio_dolares = models.CharField(max_length=20)