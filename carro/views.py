from django.shortcuts import render, redirect
from sitio import views
from .carro import Carro
from django.http import HttpResponse, HttpResponseBadRequest
import requests
from rest_framework.utils import json
from datetime import datetime
from django.contrib.auth.models import User
from venta.models import Ventas

now = datetime.now()
# Create your views here.

def agregar_producto(request, producto_id):
    
    response = requests.get('http://44.194.7.13:8000/productos/').json()
        
    for obj in response:
        
        if obj['cod_prod'] == producto_id:
            producto = [obj['cod_prod'], obj['descripcion'], obj['pr_vta'], obj['imagen']]
    
    print(producto[0])
    carro=Carro(request)
    carro.agregar(producto=producto)
    return redirect("sitio")

def eliminar_producto(request, producto_id):
    #response = requests.get('http://54.175.6.198:8000/productos').json()
        
    #for obj in response:
        
    #    if obj['cod_prod'] == producto_id:
    #        producto = [obj['cod_prod'], obj['descripcion'], obj['pr_venta'], obj['imagen']]
    carro=Carro(request)
    #producto= Producto.objects.get(id=producto_id)
     
    carro.eliminar(producto=producto_id)
    return redirect("sitio")

def restar_producto(request, producto_id):
    response = requests.get('http://44.194.7.13:8000/productos/').json()
        
    for obj in response:
        #print(obj['cod_prod'])
        if obj['cod_prod'] == producto_id:

            producto = [obj['cod_prod'], obj['descripcion'], obj['pr_vta'], obj['imagen']]
            print (producto[0])

    carro=Carro(request)
    carro.restar_producto(producto=producto)
    return redirect("sitio")

def limpiar_carro(request, producto_id):

    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("sitio")

def post_despachos(request):
    carro=Carro(request)
    total=0
    url = "http://54.236.30.202:8000/gestion/venta/crear/"
    #url = "http://54.89.245.164:8000/despachos/crear"
    #form = ProductoForm(request.POST or None)
    #self.carro=carro
    if not 'carro':
        print("VACIO")
        return redirect("sitio")
    else:
        #if form.is_valid():
        print (request.session["carro"].items())
        
        for key, value in request.session["carro"].items():
            total=total+(int(value["precio"]))
        name = User.objects.get(username=request.user).first_name
        last_name = User.objects.get(username=request.user).last_name
        nombre = name +" "+ last_name
        rut = '123456789'
        direccion = "chile sur 389 nueva aurora"
        nro_venta = "96"
        fecha_compra=(now.day, now.month, now.year)
        tipo_venta="boleta"
        estado_compra="2" 
        print(total)
        data = {'nombre_cliente': nombre, 'rut_cliente': rut, 'direccion': direccion, 'nro_venta': nro_venta, 'fecha_compra': fecha_compra,'tipo_venta':tipo_venta, 'estado_compra':estado_compra}
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        numero_bol = Ventas.objects.all().last().id
        venta = Ventas()
        venta.nombre_cliente = name +" "+ last_name
        venta.rut_cliente = "123456789"
        venta.direccion = "lejos"
        venta.nro_boleta =numero_bol + 1 
        venta.fecha_compra = (now.day, now.month, now.year)
        neto = float(total/1.19)
        iva = neto * 0.19
        venta.valor_neto = neto
        venta.valor_iva = iva
        venta.valor_total = total
        venta.save()
        #venta.success(request,'boleta creada')
        
        carro.limpiar_carro()
        

        return redirect("sitio")

        