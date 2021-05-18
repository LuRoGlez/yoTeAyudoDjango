from django.shortcuts import render
from .models import Cliente, Especialista, Cita, Mensaje
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.mail import send_mail
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