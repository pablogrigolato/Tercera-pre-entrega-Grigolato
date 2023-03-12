from django.contrib import admin
from django.urls import path
from BibliotecaVirtual import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('libros', views.libro, name='Libros'),
    path('alumnos', views.alumno, name='Alumnos'),
    path('docentes', views.docente, name='Docentes'),
]
