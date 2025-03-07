from django.db import models

# Create your models here.
class Carrito(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)
    precio_dolares = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20, null=True)
    fecha_compra = models.DateField(null=True)