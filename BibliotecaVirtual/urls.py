from django.contrib import admin
from django.urls import path
from BibliotecaVirtual.views import libro, alumno, docente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', libro),
    path('alumno/', alumno),
    path('docente/', docente),
]
