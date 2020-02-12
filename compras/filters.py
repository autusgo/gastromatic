import django_filters
from .models import Factura

class FacturaFilter(django_filters.FilterSet):
    class Meta:
        model = Factura
        fields = ['estado']
