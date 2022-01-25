import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.forms import CursoForm, ProfesorFormulario
from AppCoder.models import Curso, Profesor

def crear_curso(request, camada):
    curso = Curso(nombre='Python', camada = camada)
    curso.save()
    return HttpResponse(f'Curso creado! {camada}')


def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    

def cursos(request):
    return render(request, 'AppCoder/cursos.html', {'cursos': Curso.objects.all()})
    

def profesores(request):
    return render(request, 'AppCoder/profesores.html', {'profesores': Profesor.objects.all()})

def estudiantes(request):
    return HttpResponse('estudiantes')

def entregables(request):
    return HttpResponse('entregables')

def cursos_formulario(request):
   if request.method == 'POST':
       formulario = CursoForm(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           Curso.objects.create(nombre=data['curso'], camada=data['camada'])
           return redirect('cursos')
   
   else:
       formulario = CursoForm()
       
   return  render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario})

def profesorFormulario(request):
   if request.method == 'POST':
       miformulario = ProfesorFormulario(request.POST)

       if miformulario.is_valid():
           informacion = miformulario.cleaned_data
           Profesor.objects.create(nombre=informacion['nombre'], apellido=informacion['apellido'],
           email=informacion['email'], profesion=informacion['profesion'])
           return redirect('profesores')
   
   else:
       miformulario = ProfesorFormulario()
       
   return  render(request, 'AppCoder/profesorFormulario.html', {'miformulario': miformulario})

def busqueda_camada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    camada= request.GET.get("camada")
    
    if camada: 
        cursos = Curso.objects.filter(camada=camada)
    
        return render(request, 'AppCoder/buscar.html',
        {'cursos' : cursos, 'camada': camada})
        
    else:
        return HttpResponse ('No se envio una camada valida')