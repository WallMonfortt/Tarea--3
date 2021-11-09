from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from clase.models import Clase
from estudiante.models import Estudiante

# Create your views here.
def lista_clases(request):
  if request.method == 'GET':
    clases = Clase.objects.all()
    estudiantes = Estudiante.objects.all()
    contexto = {
      'clases': clases,
      'estudiantes': estudiantes
    }
    return render(request, 'clases/list.html', contexto)

  if request.method == 'POST':
    Clase.objects.create(
      nombre=request.POST['nombre'],
      descripcion=request.POST['descripcion'],
      turno=request.POST['turno'],

      estudiantes=request.POST.set('estudiantes')
    )
    clases = Clase.objects.all()
    estudiantes = Estudiante.objects.all()
    contexto = {
      'clases': clases,
      'estudiantes': estudiantes
    }
    return render(request, 'clases/list.html', contexto)


def clase_id(request, id):
  if request.method == 'GET':
    clase = Clase.objects.get(id=id)
    estudiantes = Estudiante.objects.all()
    contexto = {
      'clase': clase,
      'estudiantes': estudiantes
    }
    return render(request, 'clases/detalle.html', contexto)