from django.urls import path
from . import views
from .views import ProveedorListView

urlpatterns = [
    path('', ProveedorListView.as_view(), name="proveedor_list"),
    # path('', views.proveedor_list, name='proveedor_list'),
    path('proveedor/<int:pk>/', views.proveedor_detail, name='proveedor_detail'),
    path('proveedor/new/', views.proveedor_new, name='proveedor_new'),
    path('proveedor/<int:pk>/edit/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedor/<pk>/remove/', views.proveedor_remove, name='proveedor_remove'),
]
