from django.contrib import admin
from django.urls import path
from BibliotecaVirtual import views

urlpatterns = [
    path('', views.inicio),
    path('libro/', views.libro),
    path('alumno/', views.alumno),
    path('docente/', views.docente),
]
