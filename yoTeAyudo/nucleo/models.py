from django.db import models


class Usuario(models.Model):
    username=models.CharField(max_length=30)
    password=models.IntegerField(max_length=30)

class Cliente (models.Model):
    dni=models.CharField(max_length=9)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    fechaNacimiento=models.DateField
    foto=models.ImageField(upload_to='photos/', verbose_name="Foto")
    idUsuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Especialista (models.Model):
    dni=models.CharField(max_length=9)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    direccion=models.CharField(max_length=80)
    fechaNacimiento=models.DateField
    foto=models.ImageField(upload_to='photos/', verbose_name="Foto")
    biografia=models.TextField(max_length=255)
    idUsuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)


class Citas(models.Model):
    fecha=models.DateField
    idCliente=models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    idEspecialista=models.ForeignKey(Especialista, verbose_name="Especialista", on_delete=models.CASCADE)

class Mensajes(models.Model):
    idEmisor=models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.CASCADE)
    idReceptor=models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.CASCADE)
    fecha=models.DateField
    asunto=models.CharField(max_length=50)
    texto=models.TextField