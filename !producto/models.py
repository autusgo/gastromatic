from django.db import models

# Create your models here.
from django.conf import settings
from decimal import Decimal

class Producto(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=9 , decimal_places=2)
    unidad_de_medida = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.presentacion)


class Detalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5 , decimal_places=0)
    precio = models.DecimalField(max_digits=9 , decimal_places=2)

    @property
    def precio_total(self):
        return F(cantidad) * F(precio)

    #def __str__(self):
    #    return '{} {}'.format(self.producto, self.precio_total)

    #class Meta:
    #    ordering = ['producto']
