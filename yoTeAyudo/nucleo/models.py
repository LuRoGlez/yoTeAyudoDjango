from django.db import models


class Usuario(models.Model):
    username=models.CharField(max_length=30)
    password=models.IntegerField(max_length=30)

class Cliente (models.Model):
    dni=models.CharField(max_length=9)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    direccion=models.CharField(max_length=80)
    fechaNacimiento=models.DateField(max_length=30)
    foto=models.ImageField(upload_to='photos/', verbose_name="Foto")
    idUsuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)