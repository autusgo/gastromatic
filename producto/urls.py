from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
]
