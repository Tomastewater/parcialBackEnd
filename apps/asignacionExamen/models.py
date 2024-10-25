from django.db import models

class asignacionExamen(models.Model):
    fechaAsignacion = models.DateField(auto_now=True)
    fechaResolucion = models.DateField(auto_created=False)
    calificacion = models.DecimalField(max_digits=2)
    observaciones = models.TextField(max_length=200)
    examen = models.ForeignKey("examen.Examen", on_delete=models.CASCADE)
    alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fechaAsignacion}, {self.fechaResolucion}, {self.calificacion}, {self.observaciones}, {self.examen}, {self.alumno}"
