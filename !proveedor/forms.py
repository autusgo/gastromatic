from django import forms

from .models import Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ('apellido','nombre', 'CUIT', 'dirección', 'teléfono','correo_electrónico')
