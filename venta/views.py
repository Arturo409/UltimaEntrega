from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers

from .models import Ventas
from .serializers import ventaSerializers
from rest_framework.decorators import api_view

@api_view(['GET'])
def VentasLista(request):
    ventas = Ventas.objects.all()
    serializer = ventaSerializers(ventas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def VentasDetalle(request, pk):
    ventas = Ventas.objects.get(id=pk)
    serializer = ventaSerializers(ventas, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def VentasActualizar(request, pk):
    ventas = Ventas.objects.get(id=pk)
    serializer = ventaSerializers(instance=ventas, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])
def VentasCrear(request):
    serializers = ventaSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    else:
        return Response(serializers.errors)
    return Response(serializers.data)

@api_view(['DELETE'])
def VentasEliminar(request, pk):
    ventas = Ventas.objects.get(id=pk)
    ventas.delete()
    return Response('Eliminado')
