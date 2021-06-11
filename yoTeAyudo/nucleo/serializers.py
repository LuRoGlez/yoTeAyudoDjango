from rest_framework import  serializers
from .models import Especialista, Cliente, Cita, Mensaje

class CitaSerializers (serializers.ModelSerializer):
    #current_user = serializers.SerializerMethodField('get_user')

    class Meta:
        model = Cita
        fields = ('id', 'fecha', 'idCliente', 'idEspecialista', 'informe', 'realizada')
        depth = 4
    
   # def get_user(self):
    #    request = self.context
     #   return request.user

        
class EspecialistaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields =['id', 'nombre', 'apellidos']