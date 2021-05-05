from django.shortcuts import render
from .models import Cliente, Especialista, Cita, Mensaje
from django.views.generic.list import ListView
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, 'nucleo/index.html', {})

class EspecialistaListView(ListView):
    model=Especialista