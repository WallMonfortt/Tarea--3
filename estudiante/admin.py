from django.contrib import admin
from clase.models import Clase

from estudiante.models import Estudiante


# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Clase)
# admin.site.register(EstudiantesClase)
