from django.shortcuts import render

from estudiante.models import Estudiante

# Create your views here.

def lista_estudiantes(request):
  if request.method == 'GET':
    estudiantes = Estudiante.objects.all()
    contexto = {
      'estudiantes': estudiantes
    }
    
    return render(request, 'estudiantes/lista.html', contexto)

  if request.method == 'POST':
    Estudiante.objects.create(
      nombre=request.POST['nombre'], 
      apellido=request.POST['apellido'],
      edad=request.POST['edad'],
      genero = request.POST['genero'],
      telefono = request.POST['telefono'],
      email = request.POST['email'],
    )

    estudiantes = Estudiante.objects.all()
    contexto = {
      'estudiantes': estudiantes
    }
    return render(request, 'estudiantes/lista.html', contexto)

def estudiante_id(request, id):
  estudiante = Estudiante.objects.get(id=id)
  return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})