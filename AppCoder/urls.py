from django.urls import path

from AppCoder.views import crear_curso, cursos, inicio

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio),
    path('cursos', cursos),
]