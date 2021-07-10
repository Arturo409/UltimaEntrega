from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.VentasLista, name="ventas"),
    path('detalle/<str:pk>', views.VentasDetalle, name="detalle"),
    path('crear', views.VentasCrear, name="crear"),
    path('actualizar/<str:pk>', views.VentasActualizar, name="actualizar"),
    path('eliminar/<str:pk>', views.VentasEliminar, name="eliminar"),
]