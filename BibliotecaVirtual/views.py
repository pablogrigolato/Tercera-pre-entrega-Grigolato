from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaVirtual.models import Libro, Alumno, Docente
from BibliotecaVirtual.forms import LibroFormulario, AlumnoFormulario, DocenteFormulario

# Create your views here.

def inicio(request):
    return render(request, "BibliotecaVirtual/inicio.html")

def libro(request):
    return render(request, "BibliotecaVirtual/libros.html")

def alumno(request):
    return render(request, "BibliotecaVirtual/alumnos.html")

def docente(request):
    return render(request, "BibliotecaVirtual/docentes.html")

def libroFormulario(request):
    if request.method == 'POST': 
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro(nombre=request.POST['nombre'],
                      autor=request.POST['autor'],
                      codigo=request.POST['codigo']
                      )
            libro.save()
            return render(request, "BibliotecaVirtual/inicio.html")
        
    else:
        miFormulario = LibroFormulario()
            
    return render(request,"BibliotecaVirtual/libroFormulario.html", {"miFormulario": miFormulario})

def alumnoFormulario(request):
    if request.method == 'POST': 
        miFormulario = AlumnoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumno = Alumno(nombre=request.POST['nombre'],
                      apellido=request.POST['apellido'],
                      dni=request.POST['dni'],
                      email=request.POST['email']
                      )
            alumno.save()
            return render(request, "BibliotecaVirtual/inicio.html")
        
    else:
        miFormulario = AlumnoFormulario()
            
    return render(request,"BibliotecaVirtual/alumnoFormulario.html", {"miFormulario": miFormulario})

def docenteFormulario(request):
    if request.method == 'POST': 
        miFormulario = DocenteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumno = Docente(nombre=request.POST['nombre'],
                      apellido=request.POST['apellido'],
                      dni=request.POST['dni'],
                      email=request.POST['email'],
                      asignatura=request.POST['asignatura']
                      )
            alumno.save()
            return render(request, "BibliotecaVirtual/inicio.html")
        
    else:
        miFormulario = DocenteFormulario()
            
    return render(request,"BibliotecaVirtual/docenteFormulario.html", {"miFormulario": miFormulario})
