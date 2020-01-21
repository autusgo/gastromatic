from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from .models import Proveedor
from .forms import ProveedorForm
from django.shortcuts import redirect

# PRODUCTOS
def product_list(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'producto/product_list.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/producto_detail.html', {'producto': producto})

def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            producto.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'producto/producto_edit.html', {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            producto.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto/producto_edit.html', {'form': form})

def producto_remove(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('product_list')

#PROVEEDORES
def proveedor_list(request):
    proveedores = Proveedor.objects.all().order_by('apellido')
    return render(request, 'proveedor/proveedor_list.html', {'proveedores': proveedores})

def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/proveedor_detail.html', {'proveedor': proveedor})

def proveedor_new(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            proveedor.save()
            return redirect('proveedor_detail', pk=proveedor.pk)
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/proveedor_edit.html', {'form': form})

def proveedor_edit(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            proveedor.save()
            return redirect('proveedor_detail', pk=proveedor.pk)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor/proveedor_edit.html', {'form': form})

def proveedor_remove(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect('proveedor_list')
