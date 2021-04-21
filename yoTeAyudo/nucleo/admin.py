from django.contrib import admin
from nucleo.models import Cliente, Especialista, Cita, Mensaje

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Especialista)
admin.site.register(Cita)
admin.site.register(Mensaje)
