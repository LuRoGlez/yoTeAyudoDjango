from django import forms
from .models import Mensaje, Cita

class FormularioMensaje (forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('idReceptor', 'asunto', 'texto')