from django import forms
from .models import Mensaje, Cita

class FormularioMensaje (forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('idReceptor', 'asunto', 'texto')

class FormularioInforme (forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('informe',)

class FormularioAplazarCita (forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha',)