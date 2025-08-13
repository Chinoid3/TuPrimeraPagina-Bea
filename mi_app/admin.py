from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento')
    list_filter = ('nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'fecha_publicacion', 'precio')
    list_filter = ('genero', 'fecha_publicacion', 'autor')
    search_fields = ('titulo', 'isbn', 'autor__nombre', 'autor__apellido')