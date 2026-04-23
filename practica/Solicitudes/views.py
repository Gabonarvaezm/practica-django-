from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Solicitud
from .forms import SolicitudForm


# LISTAR SOLICITUDES
@login_required
def lista_solicitudes(request):
    solicitudes = Solicitud.objects.filter(usuario=request.user)
    return render(request, 'solicitudes/lista_solicitudes.html', {
        'solicitudes': solicitudes
    })


# CREAR SOLICITUD
@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return redirect('lista_solicitudes')
    else:
        form = SolicitudForm()

    return render(request, 'solicitudes/solicitudes_form.html', {
        'form': form
    })


# DETALLE DE SOLICITUD
@login_required
def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk, usuario=request.user)
    return render(request, 'solicitudes/detalle_solicitud.html', {
        'solicitud': solicitud
    })


# EDITAR SOLICITUD
@login_required
def editar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('detalle_solicitud', pk=pk)
    else:
        form = SolicitudForm(instance=solicitud)

    return render(request, 'solicitudes/solicitudes_form.html', {
        'form': form
    })


# ELIMINAR SOLICITUD
@login_required
def eliminar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk, usuario=request.user)

    if request.method == 'POST':
        solicitud.delete()
        return redirect('lista_solicitudes')

    return render(request, 'solicitudes/confirmar_eliminacion.html', {
        'solicitud': solicitud
    })