from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.
def product_list(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'producto/product_list.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/producto_detail.html', {'producto': producto})
