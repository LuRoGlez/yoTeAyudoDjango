from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Especialista, Cita, Mensaje
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.mail import send_mail
from nucleo.forms import FormularioMensaje
from datetime import datetime

now=datetime.now()
# Create your views here.
def index(request):
    return render(request, 'nucleo/index.html', {})

class EspecialistaListView(ListView):
    model=Especialista

class CitaCreateView(CreateView):
    model=Cita
    fields=['fecha', 'idCliente', 'idEspecialista']
    success_url="/nucleo/listCita"

class EspecialistaDetailView(DetailView):
    model=Especialista

class CitaListView(ListView):
    model=Cita

class CitaUpdateView(UpdateView):
    model=Cita
    fields=['fecha', 'idEspecialista']
    success_url="/nucleo/listCita"

class CitaDeleteView(DeleteView):
    model=Cita
    success_url="/nucleo/listCita"

class ClienteListView(ListView):
    model=Cliente

def citasCliente(request, pk):
    cliente=get_object_or_404(Cliente, id=pk)
    citas=Cita.objects.filter(idCliente=cliente)
    return render(request, "nucleo/citas_cliente.html", {'cliente':cliente, 'citas':citas})

class MensajeListView(ListView):
    model=Mensaje

class MensajeDetailView(DetailView):
    model=Mensaje


def crear_mensaje(request):
    if request.method == "POST":
        form = FormularioMensaje(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.idEmisor = request.user 
            post.save()
            return redirect("listMensaje")
        

    form = FormularioMensaje()
    return render(request, "nucleo/crear_mensaje.html", {"form":form})

def citasHoy(request):
    citas=Cita.objects.filter(fecha=now.date())
    return render(request, "nucleo/citas_hoy.html", {'citas':citas})