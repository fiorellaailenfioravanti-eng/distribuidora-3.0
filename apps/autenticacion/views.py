from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from apps.permisos.roles import es_personal_interno
from apps.permisos.views import destino_personal
from .forms import RegistroUsuarioForm, IngresarUsuarioForm


def _ya_ingresado(request):
    """Un usuario con sesión iniciada no vuelve a ver el login ni el registro."""
    if not request.user.is_authenticated:
        return None
    messages.info(request, f'Ya ingresaste como {request.user.username}.')
    if es_personal_interno(request.user):
        return redirect(destino_personal(request.user))
    return redirect('inicio')


def registrar_usuario(request):
    if (ya := _ya_ingresado(request)) is not None:
        return ya
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta se creó. Ya podés ingresar.')
            return redirect('apps.autenticacion:ingresar')
        else:
            messages.error(request, 'No se pudo crear la cuenta: revisá los campos marcados.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'autenticacion/registrar.html', {'form': form})

def ingresar_usuario(request):
    if (ya := _ya_ingresado(request)) is not None:
        return ya
    next_url = request.GET.get('next')
    if next_url and 'carrito' in next_url:
        messages.info(request, "Ingresá para ver tu carrito.")
    if request.method == 'POST':
        form = IngresarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Ingreso exitoso.')
                destino = request.POST.get('next') or next_url
                if destino and url_has_allowed_host_and_scheme(
                    destino, allowed_hosts={request.get_host()}, require_https=request.is_secure()
                ):
                    return redirect(destino)
                if es_personal_interno(user):
                    return redirect(destino_personal(user))
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos. Probá de nuevo.')
    else:
        form = IngresarUsuarioForm()
    return render(request, 'autenticacion/ingresar.html', {'form': form})

def cerrar_sesion(request):
    if request.method != 'POST':
        # Cerrar sesión por GET permitiría desloguear con un simple enlace (H-31).
        return redirect('inicio')
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('apps.autenticacion:ingresar')

@login_required
def perfil_usuario(request):
    return render(request, 'autenticacion/perfil.html')

