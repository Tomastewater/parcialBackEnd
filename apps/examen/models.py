from django.db import models

class Examen(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=True)
    asignatura = models.ForeignKey("asignatura.Asignatura", on_delete=models.CASCADE)
    profesor = models.ForeignKey("profesor.Profesor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}, {self.fecha}, {self.asignatura}, {self.profesor}"


