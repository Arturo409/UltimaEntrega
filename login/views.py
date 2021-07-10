from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Create your views here.
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sitio')
        else:
            messages.info(request,'Usuario o clave incorrecta')

    context = {}
    return render(request,"login/login.html",context)
def logoutUser(request):
    logout(request)
    return redirect('sitio')

def registro(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Cuenta creada para '+ user)
            return redirect('login')
    context = {'form':form}
    return render(request,"login/registro.html", context)

def inicio(request):
    return render (request,"sitio/index.html")
