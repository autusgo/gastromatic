import django_filters
from .models import Proveedor, Factura
from django_filters import FilterSet

class ProveedorFilter(django_filters.FilterSet):
    class Meta:
        model = Proveedor
        fields = ['apellido']

class FacturaFilter(django_filters.FilterSet):
    class Meta:
        model = Factura
        fields = ['estado']
