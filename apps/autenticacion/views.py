from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, IngresarUsuarioForm

# Create your views here.
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('apps.autenticacion:ingresar')
        else:
            messages.error(request, 'Error al registrar el usuario. Por favor, revise los datos ingresados.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'autenticacion/registrar.html', {'form': form})

def ingresar_usuario(request):
    next_url = request.GET.get('next')
    if next_url and 'carrito' in next_url:
        messages.info(request, "Debe ingresar para acceder al carrito.")
    if request.method == 'POST':
        form = IngresarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Ingreso exitoso.')
                return redirect('inicio')  # Redirigir a la página principal u otra página
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, intente de nuevo.')
    else:
        form = IngresarUsuarioForm()
    return render(request, 'autenticacion/ingresar.html', {'form': form})

def cerrar_sesion(request): 
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('apps.autenticacion:ingresar')

@login_required
def perfil_usuario(request):
    return render(request, 'autenticacion/perfil.html')

