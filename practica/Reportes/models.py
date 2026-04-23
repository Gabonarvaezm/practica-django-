from django.db import models

# Create your models here.

class Reporte(models.Model):
    nombreDelReporte = models.CharField(max_length=100)
    fechaDeGeneracion = models.DateField()
    tipoDeReporte = models.CharField(max_length=50)
    decripcion = models.TextField()
    reponsable = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombreDelReporte} - {self.fechaDeGeneracion} - {self.tipoDeReporte} - {self.descripcion} - {self.responsable}"
