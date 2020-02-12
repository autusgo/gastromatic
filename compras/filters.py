import django_filters
from .models import Proveedor
from django_filters import FilterSet

class ProveedorFilter(django_filters.FilterSet):
    class Meta:
        model = Proveedor
        fields = ['apellido']
