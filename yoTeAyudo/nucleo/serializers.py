from rest_framework import  serializers
from .models import Especialista, Cliente, Cita, Mensaje

class CitaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'idCliente', 'idEspecialista', 'informe', 'realizada']

class EspecialistaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields =['id', 'nombre', 'apellidos']