from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'presentacion', 'precio_unitario', 'unidad_de_medida')
