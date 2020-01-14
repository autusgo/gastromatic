from django.shortcuts import render
from .models import Producto

# Create your views here.
def product_list(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'producto/product_list.html', {'productos': productos})
