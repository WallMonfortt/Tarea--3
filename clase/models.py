from django.db import models

from estudiante.models import Estudiante

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200, null=True, blank=True)
    turno = models.CharField(max_length=50)
    estudiantes = models.ManyToManyField(Estudiante, related_name='EstudiantesClase')

    def __str__(self):
        return self.nombre

# class EstudiantesClase(models.Model):
#     clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True)
#     estudiantes = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.clase.nombre + ' ' + self.estudiantes.nombre