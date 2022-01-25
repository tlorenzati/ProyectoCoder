import email
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppCoder.forms import CursoForm, EstudianteForm, ProfesorFormulario
from AppCoder.models import Curso, Estudiante, Profesor

from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView


class ProfesorListView(ListView):
    model = Profesor
    template_name = 'AppCoder/profesores.html'
    context_object_name = 'profesores'
    
class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'AppCoder/ver_profesor.html'
    
class ProfesorCreateView(CreateView):    
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']  #estos atributos deben coincidir con los del modelo
    template_name = 'AppCoder/profesor_form.html'
    
class CursoCreateView(CreateView):    
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']  #estos atributos deben coincidir con los del modelo
    template_name = 'AppCoder/curso_form.html'
    
class EstudianteCreateView(CreateView):    
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']  #estos atributos deben coincidir con los del modelo
    template_name = 'AppCoder/estudiante_form.html'

class ProfesorUpdateView(UpdateView):    
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']  #estos atributos deben coincidir con los del modelo
    template_name = 'AppCoder/profesor_form.html'
    
class ProfesorDeleteView(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    #Template_name toma por default 'AppCoder/profesor_confirm_delete.html'
    
   

def crear_curso(request, camada):
    curso = Curso(nombre='Python', camada = camada)
    curso.save()
    return HttpResponse(f'Curso creado! {camada}')


def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    

def cursos(request):
    return render(request, 'AppCoder/cursos.html', {'cursos': Curso.objects.all()})
    

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html', {'estudiantes': Estudiante.objects.all()})

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

def estudiantes_formulario(request):
   if request.method == 'POST':
       formulario = EstudianteForm(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           Estudiante.objects.create(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
           return redirect('estudiantes')
   
   else:
       formulario = EstudianteForm()
       
   return  render(request, 'AppCoder/estudiante_Form.html', {'formulario': formulario})


def profesorFormulario(request): #REEMPLAZADO POR ProfesorCreateView
   if request.method == 'POST':
       formulario = ProfesorFormulario(request.POST)

       if formulario.is_valid():
           informacion = formulario.cleaned_data
           Profesor.objects.create(nombre=informacion['nombre'], apellido=informacion['apellido'],
           email=informacion['email'], profesion=informacion['profesion'])
           return redirect('profesores')
   
   else:
       formulario = ProfesorFormulario()
       
   return  render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario})

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
    
def profesores(request):
    return render(request, 'AppCoder/profesores.html', {'profesores': Profesor.objects.all()})


def profesor_delete(request, id_profe):
    profesor = Profesor.objects.get(id=id_profe)
    profesor.delete()
    
    return redirect('profesores')


def profesor_update(request, id_profe):
    profesor = Profesor.objects.get(id=id_profe)
    
    if request.method == 'POST':
       formulario = ProfesorFormulario(request.POST)

       if formulario.is_valid():
           informacion = formulario.cleaned_data
           
           profesor.nombre=informacion['nombre']
           profesor.apellido=informacion['apellido']
           profesor.email=informacion['email']
           profesor.profesion=informacion['profesion']
           profesor.save()
           
           return redirect('profesores')
   
    else:
       formulario = ProfesorFormulario(model_to_dict(profesor)) #en base a un model te hace un diccionario
       
    return  render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario})
    
    