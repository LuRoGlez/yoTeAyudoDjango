from django.shortcuts import render
from .models import Cliente, Especialista, Cita, Mensaje
# Create your views here.
def index(request):
    return render(request, 'nucleo/index.html', {})