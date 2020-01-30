from django.contrib import admin

# Register your models here.
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'nombre', 'precio_unitario', 'stock']
    list_editable = ['nombre', 'precio_unitario']
    #prepopulate_fields = {'nombre':('stock')}
admin.site.register(Producto, ProductoAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['CUIT', 'apellido', 'nombre']
    list_filter = ['apellido', ]
admin.site.register(Proveedor, ProveedorAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'numero', 'proveedor', 'detalle', 'estado']
admin.site.register(Factura, FacturaAdmin)

class DetalleAdmin(admin.ModelAdmin):
    list_display = ['cantidad', 'producto']
admin.site.register(Detalle, DetalleAdmin)
