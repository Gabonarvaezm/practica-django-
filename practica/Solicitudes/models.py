from django.db import models
from django.contrib.auth.models import User


class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('completada', 'Completada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )

    prioridad = models.IntegerField(default=1)  # 1 baja, 2 media, 3 alta

    def __str__(self):
        return f"{self.titulo} - {self.estado}"