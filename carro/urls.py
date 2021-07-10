from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import guardar_toquen

app_name="carro"

urlpatterns = [
        path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
        path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
        path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
        path("limpiar/", views.limpiar_carro, name="limpíar"),
        path("vender/", views.post_despachos, name="despachos")
]       