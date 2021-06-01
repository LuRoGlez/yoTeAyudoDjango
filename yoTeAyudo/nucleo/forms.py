from django import forms
from .models import Mensaje, Cita, Cliente, Especialista

class FormularioMensaje (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioMensaje, self).__init__(*args, **kwargs)
        self.fields['idReceptor'].queryset = Cliente.objects.all()

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

class FormularioMensajeCl (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioMensajeCl, self).__init__(*args, **kwargs)
        self.fields['idReceptor'].queryset = Especialista.objects.all()

    class Meta:
        model = Mensaje
        fields = ('idReceptor', 'asunto', 'texto')
