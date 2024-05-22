from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor
from .forms import LibroForm, AutorForm

# Create your views here.

def home(request):
    return render(request, 'libros/home.html')

#Read
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request,'libros/listar_libros.html',{'libros':libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def actualizar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/actualizar_libro.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'libros/listar_autores.html', {'autores': autores})

# Create
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'libros/crear_autor.html', {'form': form})

# Update
def actualizar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'libros/actualizar_autor.html', {'form': form})

# Delete
def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'libros/eliminar_autor.html', {'autor': autor})