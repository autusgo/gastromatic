from django.urls import path
from . import views

urlpatterns = [
    path('', views.factura_list, name='factura_list'),
    path('factura/<int:pk>/', views.factura_detail, name='factura_detail'),
    path('factura/new/', views.factura_new, name='factura_new'),
    path('factura/<int:pk>/edit/', views.factura_edit, name='factura_edit'),
    path('factura/<pk>/remove/', views.factura_remove, name='factura_remove'),
]
