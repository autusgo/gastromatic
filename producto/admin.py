from django.contrib import admin

# Register your models here.
from .models import Producto
from .models import LineaDeProducto

admin.site.register(Producto)
admin.site.register(LineaDeProducto)
