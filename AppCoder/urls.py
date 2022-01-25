from django.urls import path

from AppCoder.views import CursoCreateView, EstudianteCreateView, ProfesorCreateView, ProfesorDeleteView, ProfesorDetailView, ProfesorListView, ProfesorUpdateView, buscar, busqueda_camada, crear_curso, cursos, estudiantes, inicio, profesor_delete, cursos_formulario

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio, name='inicio'),
    path('cursos', cursos, name='cursos'),
    #path('profesores', profesores, name='profesores'),
    path('cursosFormulario', cursos_formulario, name='cursos_formulario'),
    #path('profesorFormulario', profesorFormulario, name='profesorFormulario'),
    path('busquedaCamada', busqueda_camada, name='busqueda_camada'),
    path('buscar', buscar, name='buscar'),
    #path('profesoresDelete<id_profe>', profesor_delete, name='profesor_delete'),
    #path('profesoresUpdate<id_profe>', profesor_update, name='profesor_update'),
    path('profesores', ProfesorListView.as_view(), name='profesores'),
    path('profesor/add', ProfesorCreateView.as_view(), name='profesorFormulario'),
    path('profesoresUpdate<pk>', ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesoresDelete<pk>', ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('profesoresView<pk>', ProfesorDetailView.as_view(), name='profesor_view'),
    path('cursos/add', CursoCreateView.as_view(), name='curso_Formulario'),
    path('estudiantes/add', EstudianteCreateView.as_view(), name='estudiantes_Formulario'),
    path('estudiantes', estudiantes, name='estudiantes'),
]