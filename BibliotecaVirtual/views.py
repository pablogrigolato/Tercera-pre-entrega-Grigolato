from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaVirtual.models import Libro, Alumno, Docente

# Create your views here.

def inicio(request):
    return render(request, "BibliotecaVirtual/inicio.html")

def libro(request):
    return render(request, "BibliotecaVirtual/libros.html")

def alumno(request):
    return render(request, "BibliotecaVirtual/alumnos.html")

def docente(request):
    return render(request, "BibliotecaVirtual/docentes.html")
