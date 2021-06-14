from django import forms
from django.forms import widgets
from .models import Mensaje, Cita, Cliente, Especialista, User


class FormularioMensaje (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioMensaje, self).__init__(*args, **kwargs)
        self.fields['idReceptor'].queryset = User.objects.filter(is_cliente = True)

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
        widgets = {
            'fecha': forms.SelectDateWidget()
        }

class FormularioMensajeCl (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioMensajeCl, self).__init__(*args, **kwargs)
        self.fields['idReceptor'].queryset = User.objects.filter(is_especialista = True)

    class Meta:
        model = Mensaje
        fields = ('idReceptor', 'asunto', 'texto')

class setFechas(forms.Form):
    fechaAnterior=forms.DateField(label='fechaAnterior', required=True,widget=forms.DateInput(attrs={'placeholder':'AAAA-MM-DD'}))
    fechaPosterior=forms.DateField(label='fechaPosterior', required=True,widget=forms.DateInput(attrs={'placeholder':'AAAA-MM-DD'}))