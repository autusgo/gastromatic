from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.forms import modelformset_factory
from django.urls import reverse

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
def factura_error(request):
    return render(request, 'factura/factura_error.html')

def factura_list(request):
    facturas = Factura.objects.all().order_by('fecha')
    return render(request, 'factura/factura_list.html', {'facturas': facturas})

def factura_detail(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    #factura = Factura.objects.get(pk=pk) #Esto es lo mismo que lo que está arriba pero sin el 404
    context = {'factura': factura}
    template = 'factura/factura_detail.html'
    return render(request, template, context)

def factura_new(request):
    if request.method == "POST":
        factura_form = FacturaForm(request.POST)
        detalle_formset = DetalleForm(request.POST)
        if factura_form.is_valid() and detalle_formset.is_valid():
            factura = factura_form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #detalle.subtotal = detalle.total_linea
            #factura.total = factura.total_detalles
            # subtotal = 0.00
            # for detalle in factura.productos.all():
            #     subtotal += float(detalle.precio_unitario)
            # factura.total = subtotal
            factura.save()
            for detalles in detalle_formset:
                detalles.factura_id = factura.pk
                detalles.save()
            return redirect('factura_detail', pk=factura.pk)
        else:
            return redirect('factura_error')
    else:
        factura_form = FacturaForm()
        detalle_formset=modelformset_factory(Detalle, fields=('producto', 'cantidad'))
        return render(request, 'factura/factura_edit.html', {'factura_form': factura_form, 'detalle_form': detalle_formset} )

def factura_edit(request, pk):
    # factura = get_object_or_404(Factura, id=3)
    # producto = get_object_or_404(Producto, pk=pk)
    # if not producto in factura.productos.all():
    #     factura.productos.add(producto)
    # else:
    #     #factura.detalles.remove(detalle)
    #     print('el producto no está en la factura')
    # subtotal = 0.00
    # for item in factura.productos.all():
    #     subtotal += float(item.precio_unitario)
    # factura.total = subtotal
    # factura.save()
    # return HttpResponseRedirect(reverse('factura_detail'))

    factura = get_object_or_404(Factura, pk=pk)
    if request.method == "POST":
        factura_form = FacturaForm(request.POST, instance=factura)
        if factura_form.is_valid():
            factura = factura_form.save(commit=False)
            factura.save()
            return redirect('factura_list', pk=factura.pk)
    else:
        factura_form = FacturaForm(instance=factura)
    return render(request, 'factura/factura_edit.html', {'factura_form': factura_form})

def factura_remove(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    factura.delete()
    return redirect('factura_list')

 # def detalle_edit(request, pk):
 #     detalle = get_object_or_404(Detalle, pk=pk)
 #     if request.method == "POST":
 #         form_det = DetalleForm(request.POST, instance=detalle)
 #         if form_det.is_valid():
 #             detalle = form_det.save(commit=False)
 #             detalle.save()
 #             return redirect('factura_detail', pk=detalle.pk)
 #     else:
 #         form_det = DetalleForm(instance=detalle)
 #     return render(request, 'factura/factura_edit.html', {'form_det': form_det})
