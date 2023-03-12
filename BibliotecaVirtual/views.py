from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaVirtual.models import Libro, Alumno, Docente

# Create your views here.

def libro(self):
    return HttpResponse("Libro.")

def alumno(self):
    return HttpResponse("Alumno.")

def docente(self):
    return HttpResponse("Docente.")
