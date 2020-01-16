from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/new/', views.producto_new, name='producto_new'),
    path('producto/<int:pk>/edit/', views.producto_edit, name='producto_edit'),
]
