from django.db import models

class Asistencia(models.Model):
    nombre = models.CharField(max_length=150)
    numIdenticacion = models.CharField(max_length=20)
    correo = models.EmailField()
    fechaAsistencia = models.DateField()
    horaIngreso = models.TimeField()
    horaSalida = models.TimeField()
    presente = models.BooleanField()
    observaciones = models.TextField()

    def __str__ (self):
        return f"{self.nombre} - {self.numIdenticacion} - {self.fechaAsistencia} - {self.horaIngreso} - {self.horaSalida} - {'Presente' if self.presente else 'Ausente'} - {self.observaciones}"