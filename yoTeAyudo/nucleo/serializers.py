from rest_framework import  serializers
from .models import Especialista, Cliente, Cita, Mensaje

class CitaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['fecha', 'idCliente', 'idEspecialista', 'informe', 'realizada']