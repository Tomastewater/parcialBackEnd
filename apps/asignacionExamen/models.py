from django.db import models

class asignacionExamen(models.Model):
    fechaAsignacion = models.DateField(auto_now=True)
    fechaResolucion = models.DateField(auto_created=False, null=True, blank=True)
    calificacion = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    observaciones = models.TextField(max_length=200, blank=True, null=True)
    examen = models.ForeignKey("examen.Examen", on_delete=models.CASCADE)
    alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fechaAsignacion}, {self.fechaResolucion}, {self.calificacion}, {self.observaciones}, {self.examen}, {self.alumno}"
