from django.db import models


class Usuario(models.Model):
    username=models.CharField(max_length=30)
    password=models.IntegerField
    def __str__(self):
        return self.username

class Cliente (models.Model):
    dni=models.CharField(max_length=9)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    fechaNacimiento=models.DateField
    foto=models.ImageField(upload_to='photos/', verbose_name="Foto")
    idUsuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.dni+" "+self.nombre+" "+self.apellidos+" "+self.direccion+" "+self.fechaNacimiento+" "+self.foto

class Especialista (models.Model):
    dni=models.CharField(max_length=9)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    direccion=models.CharField(max_length=80)
    fechaNacimiento=models.DateField
    foto=models.ImageField(upload_to='photos/', verbose_name="Foto")
    biografia=models.TextField(max_length=255)
    idUsuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.dni+" "+self.nombre+" "+self.apellidos+" "+self.direccion+" "+self.fechaNacimiento+" "+self.foto+" "+self.biografia


class Cita(models.Model):
    fecha=models.DateField
    idCliente=models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE, related_name='Cliente')
    idEspecialista=models.ForeignKey(Especialista, verbose_name="Especialista", on_delete=models.CASCADE, related_name='Especialista')

    def __str__(self):
        return self.fecha+" Cliente: "+self.idCliente.nombre+" "+self.idCliente.apellidos+" Especialista: "+self.idEspecialista.nombre+" "+self.idEspecialista.apellidos

class Mensaje(models.Model):
    idEmisor=models.ForeignKey(Usuario, verbose_name="Usuario Emisor", on_delete=models.CASCADE, related_name='Usuario_Emisor')
    idReceptor=models.ForeignKey(Usuario, verbose_name="Usuario Receptor", on_delete=models.CASCADE, related_name='Usuario_Receptor')
    fecha=models.DateField
    asunto=models.CharField(max_length=50)
    texto=models.TextField

    def __str__(self):
        return self.idEmisor.username+" "+self.idReceptor.username+" "+self.fecha+" asunto: "+self.asunto+" mensaje: "+self.texto