from django.urls import path
from sitio import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import guardar_toquen

urlpatterns = [
        path('', views.sitio, name= "sitio"),
        path('login',views.login, name="login"),
        path('registro',views.registro, name="registro"),
        path('carrito',views.carrito, name="carrito"),
        

]