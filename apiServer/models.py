from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    class Meta: 
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    tipo = models.CharField(max_length=20)

    class Meta: 
        db_table = 'nivel'

    def __str__(self):
        return self.tipo

class Puntaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    tiempo = models.IntegerField()  # tiempo en segundos
    puntos = models.IntegerField()

    class Meta: 
        db_table = 'puntaje'

    def __str__(self):
        return f'{self.usuario.nombre} - {self.nivel.tipo} - {self.puntos} puntos'
