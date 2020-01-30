from django.contrib import admin

# Register your models here.
from .models import Producto
from .models import Detalle

admin.site.register(Producto)
admin.site.register(Detalle)
