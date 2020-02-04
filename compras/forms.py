from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'tipo', 'precio_unitario', 'unidad_de_medida')
        # widgets = {'especificaciones': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('apellido','nombre', 'CUIT', 'dirección', 'teléfono','correo_electrónico')

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('fecha','numero','proveedor', 'estado')
        labels = { 'numero': 'Número' }
        help_texts = { 'numero': '0001-00000001' }

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ('producto','cantidad')
