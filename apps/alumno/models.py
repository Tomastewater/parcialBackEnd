from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField( max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    numeroIdentificacion = models.BigIntegerField(max_length=10000)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.email}, {self.numeroIdentificacion}"
