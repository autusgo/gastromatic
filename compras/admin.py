from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Factura)
admin.site.register(Detalle)
