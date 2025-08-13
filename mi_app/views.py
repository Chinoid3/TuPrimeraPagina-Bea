from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from .models import Libro, Autor
from .forms import LibroForm, AutorForm

def index(request):
    return render(request, 'index.html')

# Vistas para Libros
def libro_list(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(
            Q(titulo__icontains=query) | 
            Q(autor__nombre__icontains=query) |
            Q(autor__apellido__icontains=query) |
            Q(genero__icontains=query)
        )
    else:
        libros = Libro.objects.all()
    
    return render(request, 'mi_app/libro_list.html', {'libros': libros, 'query': query})

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente!')
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'mi_app/libro_create.html', {'form': form})

def libro_delete(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        titulo = libro.titulo
        libro.delete()
        messages.success(request, f'Libro "{titulo}" eliminado exitosamente!')
        return redirect('libro_list')
    return render(request, 'mi_app/libro_delete.html', {'libro': libro})

# Vistas para Autores
def autor_list(request):
    query = request.GET.get('q')
    if query:
        autores = Autor.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) |
            Q(nacionalidad__icontains=query)
        )
    else:
        autores = Autor.objects.all()
    
    return render(request, 'mi_app/autor_list.html', {'autores': autores, 'query': query})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente!')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'mi_app/autor_create.html', {'form': form})

def autor_delete(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        nombre_completo = f"{autor.nombre} {autor.apellido}"
        # Verificar si el autor tiene libros antes de eliminar
        if autor.libros.exists():
            messages.error(request, f'No se puede eliminar el autor "{nombre_completo}" porque tiene libros asociados.')
            return redirect('autor_list')
        autor.delete()
        messages.success(request, f'Autor "{nombre_completo}" eliminado exitosamente!')
        return redirect('autor_list')
    return render(request, 'mi_app/autor_delete.html', {'autor': autor})