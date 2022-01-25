from django.forms import EmailField, Form, CharField, IntegerField

class CursoForm(Form):
    curso = CharField()
    camada = IntegerField()
    
class ProfesorFormulario(Form):
    nombre= CharField()
    apellido= CharField()
    email= EmailField()
    profesion= CharField()
    