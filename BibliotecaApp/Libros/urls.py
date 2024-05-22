from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/actualizar/<int:id>/', views.actualizar_libro, name='actualizar_libro'),
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/actualizar/<int:id>/', views.actualizar_autor, name='actualizar_autor'),
    path('autores/eliminar/<int:id>/', views.eliminar_autor, name='eliminar_autor'),
]