from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.forms import formset_factory, inlineformset_factory
from django.urls import reverse
import time

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
def detalle_new(request, pk):
    factuid = Factura.objects.get(pk=pk)
    DetalleFormSet = inlineformset_factory(Factura, Detalle, fields=('producto', 'cantidad',), can_delete=False)
    if request.method == "POST":
        detalle_formset = DetalleFormSet(request.POST, instance=factuid)
        if detalle_formset.is_valid():
            detalles = detalle_formset.save(commit=False)
            detalles_tot=0.00
            nuevostock=0
            for detalle in detalles:
                subtotal=detalle.total_linea()
                detalle.subtotal=subtotal
                detalles_tot+=float(subtotal)
                detalle.save()
                idpr=detalle.producto_id #tengo el id del producto que quiero modificar
                prodid=Producto.objects.get(id=idpr) #busco el producto por ese id y guardo la instancia en proid
                nuevostock=int(prodid.stock)
                nuevostock+=int(detalle.cantidad)
                prodid.stock=nuevostock
                prodid.save()
            factuid.total=detalles_tot
            factuid.save()
            return redirect('factura_detail', pk=pk)
        else:
            print('detalle_formset no es válida')
    else:
        DetalleFormSet = inlineformset_factory(Factura, Detalle, fields=('producto', 'cantidad',), can_delete=False, extra=5)
        detalle_formset = DetalleFormSet(instance=factuid)
    args = {}
    args['detalle_formset'] = detalle_formset
    return render(request, 'factura/detalle_new.html', args)


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
        if factura_form.is_valid():
            factura = factura_form.save()
            factura.save()
            return redirect('detalle_new', pk=factura.pk)
        else:
            print('factura_form no es válida')
    else:
        factura_form = FacturaForm()
    args = {}
    args['factura_form'] = factura_form
    return render(request, 'factura/factura_edit.html', args)

def factura_edit(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalle = Detalle.objects.filter(id=factura.id).first()
    if request.method == "POST":
        factura_form = FacturaEditForm(request.POST, instance=factura)
        detalle_form = DetalleEditForm(request.POST, instance=detalle)
        if factura_form.is_valid() and detalle_form.is_valid():
            factura = factura_form.save(commit=False)
            factura.save()
            return redirect('factura_list', pk=factura.pk)
    else:
        factura_form = FacturaEditForm(instance=factura)
        detalle_form = DetalleEditForm(instance=detalle)
    return render(request, 'factura/factura_edit.html', {'factura_form': factura_form, 'detalle_form': detalle_form})

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
