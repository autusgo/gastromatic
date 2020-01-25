from django.db import models

# Create your models here.
from django.conf import settings
from decimal import Decimal
from localflavor.ar.forms import ARCUITField
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from model_utils import Choices
from model_utils.fields import MonitorField
from django.utils.translation import ugettext_lazy as _

#PRODUCTOS
class Producto(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=9 , decimal_places=2)
    unidad_de_medida = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.tipo)

class LineaDeProducto(models.Model):
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

#PROVEEDORES
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

#FACTURAS
class Factura(models.Model):

    FACTURA_ESTADO = Choices(
        ('nopago', _(u'NO PAGO')),
        ('pago', _(u'PAGO')),
        #('PAGO PARCIAL', _(u'pagoparcial'))
    )

    fecha = models.DateField(default=datetime.date.today)
    numero = models.CharField(max_length=10, default='0000000000')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5 , decimal_places=0)
    monto = models.DecimalField(max_digits=9 , decimal_places=2)
    #total = models.DecimalField(max_digits=5 , decimal_places=2)
    estado = models.CharField(_(u'estado'), choices=FACTURA_ESTADO, max_length=64, default=FACTURA_ESTADO.nopago)
    fecha_de_pago = MonitorField(monitor='estado', when=[FACTURA_ESTADO.pago], verbose_name=_(u'Fecha de pago'), blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Facturas"

    def __str__(self):
        return '{} {} {}'.format(self.numero, self.monto, self.estado)

    @property
    def total(self):
        total = round(self.monto * self.cantidad, 2)
        return round(total, 2)
