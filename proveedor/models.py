from django.db import models

# Create your models here.
from django.conf import settings
from localflavor.ar.forms import ARCUITField
from phonenumber_field.modelfields import PhoneNumberField


class Proveedor(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    CUIT = models.CharField(max_length=13)
    teléfono = models.CharField(max_length=10)
    correo_electrónico = models.EmailField(max_length=100)
    dirección = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return '{} {} {}'.format(self.CUIT, self.apellido, self.nombre)
