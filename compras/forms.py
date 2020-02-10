from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'precio_unitario', 'unidad_de_medida', 'stock']
        # widgets = {'especificaciones': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['apellido','nombre', 'CUIT', 'dirección', 'teléfono','correo_electrónico']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['fecha','numero','proveedor', 'estado']
        total = forms.DecimalField(disabled=True)

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['producto','cantidad']
    #subtotal = forms.DecimalField(disabled=True)

class DetalleEditForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['producto','cantidad']
    producto = forms.CharField(disabled=True)
    cantidad = forms.IntegerField(disabled=True)

class FacturaEditForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['fecha','numero','proveedor', 'estado']
    fecha = forms.DateField(disabled=True)
    proveedor = forms.CharField(disabled=True)
    numero = forms.DecimalField(disabled=True)
