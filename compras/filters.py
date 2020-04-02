import django_filters
from .models import Proveedor, Factura, Producto
from django_filters import FilterSet

class ProveedorFilter(django_filters.FilterSet):
    class Meta:
        model = Proveedor
        fields = ['apellido']

class FacturaFilter(django_filters.FilterSet):
    class Meta:
        model = Factura
        fields = ['estado', 'proveedor']

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = ['tipo']
