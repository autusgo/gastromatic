from django import forms
from .models import Producto
from .models import Proveedor
from .models import Factura

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'tipo', 'precio_unitario', 'unidad_de_medida')

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ('apellido','nombre', 'CUIT', 'dirección', 'teléfono','correo_electrónico')

class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields = ('numero','author', 'proveedor', 'producto', 'cantidad','monto', 'estado', 'fecha')
