from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import redirect

# Create your views here.
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
