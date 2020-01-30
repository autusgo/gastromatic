from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.forms import inlineformset_factory

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

#DETALLES
#def detalle_item(request, pk):
    #producto = get_object_or_404(Producto, pk=pk)
    #precio_total = get_object_or_404(Detalle, pk=pk)

#FACTURAS
def factura_list(request):
    facturas = Factura.objects.all().order_by('fecha')
    return render(request, 'factura/factura_list.html', {'facturas': facturas})

def factura_detail(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'factura/factura_detail.html', {'factura': factura})

def factura_new(request):
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            factura.save()
            return redirect('factura_detail', pk=factura.pk)
    else:
        form = FacturaForm()
    return render(request, 'factura/factura_edit.html', {'form': form})

def factura_edit(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == "POST":
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            factura = form.save(commit=False)
            factura.save()
            return redirect('factura_detail', pk=factura.pk)
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'factura/factura_edit.html', {'form': form})

def factura_remove(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    factura.delete()
    return redirect('factura_list')
