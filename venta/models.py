from django.db import models
from django.db.models.base import Model
from django.utils import timezone


# Create your models here.

class Ventas(models.Model):
    nombre_cliente = models.CharField(max_length = 100, default = 'NOMBRE COMPLETO')
    rut_cliente = models.CharField(max_length = 11, default = 'RUT')
    direccion = models.CharField(max_length = 100, default = 'DIRECCION')
    nro_boleta = models.CharField(max_length = 11, default = 'NUMERO BOLETA')
    fecha_compra = models.DateField(auto_now=True)
    valor_neto = models.IntegerField()
    valor_iva = models.IntegerField()
    valor_total = models.IntegerField()
    
    class Meta:
        db_table = 'venta'

    def __str__(self):
        return self.nro_boleta

    