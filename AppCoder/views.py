from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

def crear_curso(request, camada):
    curso = Curso(nombre='Python', camada = camada)
    curso.save()
    return HttpResponse(f'Curso creado! {camada}')


def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    

def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    

def profesores(request):
    return HttpResponse('profesores')

def estudiantes(request):
    return HttpResponse('estudiantes')

def entregables(request):
    return HttpResponse('entregables')
