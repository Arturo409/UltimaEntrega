from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import requests


# Create your views here.

def sitio(request):
    url = ('http://44.194.7.13:8000')
    response = requests.get('http://44.194.7.13:8000/productos/').json()
        
    return render(request, "sitio/index.html", {
            'response': response,
            'url': url
    })


def login(request):
        return render(request,"login/login.html")

def registro(request):
        return render(request,"login/registro.html")

def carrito(request):
        return render(request, "sitio/carrito.html")

