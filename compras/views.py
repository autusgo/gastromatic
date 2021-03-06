from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.forms import modelformset_factory, formset_factory, inlineformset_factory
from django.urls import reverse
import time
from django.views.generic import (ListView, DetailView)
from .filters import ProveedorFilter, FacturaFilter, ProductoFilter

# PRODUCTOS
# def product_list(request):
#     productos = Producto.objects.all().order_by('nombre')
#     return render(request, 'producto/product_list.html', {'productos': productos})

def product_list(request):
    productos = ProductoFilter(request.GET, queryset=Producto.objects.all())
    return render(request, 'producto/product_list.html', {'filter': productos})

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
    proveedores = ProveedorFilter(request.GET, queryset=Proveedor.objects.all())
    return render(request, 'proveedor/proveedor_list.html', {'filter': proveedores})

# class ProveedorListView(ListView):
#     model = Proveedor
#     template = 'proveedor/proveedor_list.html'
#     proveedores = Proveedor.objects.all()

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
    DetalleFormSet = inlineformset_factory(Factura, Detalle, fields=('producto', 'cantidad',), can_delete=False, min_num=1, validate_min=True)
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
            proveid=factuid.proveedor_id #agarro el id del proveedor desde la factura
            proveedorinstance=Proveedor.objects.get(id=proveid) #uso el id para levantar el objeto Proveedor y lo guardo en proveedorinstance
            nuevadeuda=int(proveedorinstance.deuda) #guardo lo que haya ya guardado en la deuda del proveedor en nuevadeuda
            nuevadeuda+=int(factuid.total) #actualizo lo que ya haya sumándole la nueva factura
            proveedorinstance.deuda=nuevadeuda
            proveedorinstance.save()
            factuid.save()
            return redirect('factura_detail', pk=pk)
        else:
            print('detalle_formset no es válida')
    else:
        DetalleFormSet = inlineformset_factory(Factura, Detalle, fields=('producto', 'cantidad',), can_delete=False, extra=10)
        detalle_formset = DetalleFormSet(instance=factuid)
    args = {}
    args['detalle_formset'] = detalle_formset
    return render(request, 'factura/detalle_new.html', args)


#FACTURAS
def factura_error(request):
    return render(request, 'factura/factura_error.html')

def factura_list(request):
    facturas = FacturaFilter(request.GET, queryset=Factura.objects.all())
    return render(request, 'factura/factura_list.html', {'filter': facturas})

def factura_detail(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    #factura = Factura.objects.get(pk=pk) #Esto es lo mismo que lo que está arriba pero sin el 404
    detalles = Detalle.objects.filter(factura=pk)
    context = {'factura': factura, 'detalles' : detalles}
    template = 'factura/factura_detail.html'
    return render(request, template, context)

def factura_new(request):
    DetalleFormSet = modelformset_factory(Detalle, fields=('producto','cantidad'), min_num=1, validate_min=True, extra=2)
    if request.method == "POST":
        factura_form = FacturaForm(request.POST)
        detalle_formset = DetalleFormSet(request.POST)
        if factura_form.is_valid() and detalle_formset.is_valid():
            factura = factura_form.save()
            detalles = detalle_formset.save(commit=False)
            factuid = factura.id
            for det in detalles:
                det.factura = factura
                det.subtotal = det.total_linea()
                det.save()
            deta = get_object_or_404(Detalle, factura_id=factuid)
            factura.total = deta.total_detalle(factuid)
            factura.save()
            return redirect('factura_detail', pk=factura.pk)
    else:
        factura_form = FacturaForm()
        detalle_formset=DetalleFormSet(queryset=Detalle.objects.none())
    return render(request, 'factura/factura_new.html', {'factura_form': factura_form, 'detalle_formset': detalle_formset} )


def factura_edit(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == "POST":
        factura_form = FacturaEditForm(request.POST, instance=factura)
        if factura_form.is_valid():
            print('factura_form is valid')
            factura = factura_form.save(commit=False)
            if factura.estado == 'PAGA':
                nuevadeuda=0
                proveid=factura.proveedor_id #agarro el id del proveedor desde la factura
                proveedorinstance=Proveedor.objects.get(id=proveid) #uso el id para levantar el objeto Proveedor y lo guardo en proveedorinstance
                nuevadeuda=int(proveedorinstance.deuda) #guardo lo que haya ya guardado en la deuda del proveedor en nuevadeuda
                nuevadeuda-=int(factura.total) #actualizo lo que ya haya sumándole la nueva factura
                proveedorinstance.deuda=nuevadeuda
                proveedorinstance.save()
            factura.save()
            return redirect('factura_detail', pk=pk)
        else:
            print('factura_form is NOT valid')
    else:
        factura_form = FacturaEditForm(instance=factura)
    return render(request, 'factura/factura_edit.html', {'factura_form': factura_form, 'factura' : factura})

def factura_remove(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    factura.delete()
    return redirect('factura_list')
