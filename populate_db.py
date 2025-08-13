#!/usr/bin/env python
"""
Script para poblar la base de datos con datos de ejemplo
"""
import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from mi_app.models import Autor, Libro

def crear_datos_ejemplo():
    print("Creando datos de ejemplo...")
    
    # Crear autores
    autores = [
        {
            'nombre': 'Gabriel',
            'apellido': 'García Márquez',
            'nacionalidad': 'Colombiana',
            'fecha_nacimiento': date(1927, 3, 6),
            'biografia': 'Escritor, guionista, editor y periodista colombiano. Premio Nobel de Literatura en 1982.'
        },
        {
            'nombre': 'Jorge Luis',
            'apellido': 'Borges',
            'nacionalidad': 'Argentina',
            'fecha_nacimiento': date(1899, 8, 24),
            'biografia': 'Escritor, poeta, ensayista y traductor argentino, una de las figuras clave de la literatura hispanoamericana.'
        },
        {
            'nombre': 'Isabel',
            'apellido': 'Allende',
            'nacionalidad': 'Chilena',
            'fecha_nacimiento': date(1942, 8, 2),
            'biografia': 'Escritora chilena, considerada una de las autoras más importantes de la literatura latinoamericana.'
        },
        {
            'nombre': 'Mario',
            'apellido': 'Vargas Llosa',
            'nacionalidad': 'Peruana',
            'fecha_nacimiento': date(1936, 3, 28),
            'biografia': 'Escritor peruano, Premio Nobel de Literatura en 2010. Considerado uno de los más importantes novelistas y ensayistas contemporáneos.'
        },
        {
            'nombre': 'Julio',
            'apellido': 'Cortázar',
            'nacionalidad': 'Argentina',
            'fecha_nacimiento': date(1914, 8, 26),
            'biografia': 'Escritor, traductor e intelectual argentino. Considerado uno de los autores más innovadores y originales de su tiempo.'
        }
    ]
    
    # Crear autores en la base de datos
    autores_creados = []
    for autor_data in autores:
        autor, created = Autor.objects.get_or_create(
            nombre=autor_data['nombre'],
            apellido=autor_data['apellido'],
            defaults=autor_data
        )
        if created:
            print(f"Autor creado: {autor}")
        autores_creados.append(autor)
    
    # Crear libros
    libros = [
        {
            'titulo': 'Cien años de soledad',
            'autor': autores_creados[0],  # García Márquez
            'genero': 'ficcion',
            'fecha_publicacion': date(1967, 6, 5),
            'isbn': '9788497592208',
            'precio': 25.99,
            'sinopsis': 'La historia de la familia Buendía a lo largo de siete generaciones en el pueblo ficticio de Macondo.'
        },
        {
            'titulo': 'El amor en los tiempos del cólera',
            'autor': autores_creados[0],  # García Márquez
            'genero': 'romance',
            'fecha_publicacion': date(1985, 3, 1),
            'isbn': '9788497592215',
            'precio': 22.50,
            'sinopsis': 'Una historia de amor que dura más de cincuenta años entre Florentino Ariza y Fermina Daza.'
        },
        {
            'titulo': 'Ficciones',
            'autor': autores_creados[1],  # Borges
            'genero': 'ficcion',
            'fecha_publicacion': date(1944, 1, 1),
            'isbn': '9788497592222',
            'precio': 18.75,
            'sinopsis': 'Colección de cuentos que incluye obras maestras como "El jardín de senderos que se bifurcan" y "Artificios".'
        },
        {
            'titulo': 'El Aleph',
            'autor': autores_creados[1],  # Borges
            'genero': 'ficcion',
            'fecha_publicacion': date(1949, 1, 1),
            'isbn': '9788497592239',
            'precio': 19.99,
            'sinopsis': 'Colección de cuentos que incluye el famoso relato "El Aleph", donde se describe un punto que contiene todos los puntos del universo.'
        },
        {
            'titulo': 'La casa de los espíritus',
            'autor': autores_creados[2],  # Allende
            'genero': 'ficcion',
            'fecha_publicacion': date(1982, 1, 1),
            'isbn': '9788497592246',
            'precio': 24.50,
            'sinopsis': 'La historia de la familia Trueba a lo largo de cuatro generaciones, desde principios del siglo XX hasta la década de 1970.'
        },
        {
            'titulo': 'Eva Luna',
            'autor': autores_creados[2],  # Allende
            'genero': 'ficcion',
            'fecha_publicacion': date(1987, 1, 1),
            'isbn': '9788497592253',
            'precio': 21.75,
            'sinopsis': 'La historia de Eva Luna, una joven que cuenta historias para sobrevivir en un mundo lleno de injusticias.'
        },
        {
            'titulo': 'La ciudad y los perros',
            'autor': autores_creados[3],  # Vargas Llosa
            'genero': 'ficcion',
            'fecha_publicacion': date(1963, 1, 1),
            'isbn': '9788497592260',
            'precio': 23.25,
            'sinopsis': 'La historia de un grupo de cadetes en el Colegio Militar Leoncio Prado de Lima, Perú.'
        },
        {
            'titulo': 'Conversación en La Catedral',
            'autor': autores_creados[3],  # Vargas Llosa
            'genero': 'ficcion',
            'fecha_publicacion': date(1969, 1, 1),
            'isbn': '9788497592277',
            'precio': 26.99,
            'sinopsis': 'Una novela que explora la corrupción política y social del Perú durante la dictadura de Manuel Odría.'
        },
        {
            'titulo': 'Rayuela',
            'autor': autores_creados[4],  # Cortázar
            'genero': 'ficcion',
            'fecha_publicacion': date(1963, 6, 28),
            'isbn': '9788497592284',
            'precio': 27.50,
            'sinopsis': 'Una novela experimental que puede leerse de múltiples maneras, siguiendo diferentes órdenes de capítulos.'
        },
        {
            'titulo': 'Bestiario',
            'autor': autores_creados[4],  # Cortázar
            'genero': 'ficcion',
            'fecha_publicacion': date(1951, 1, 1),
            'isbn': '9788497592291',
            'precio': 20.25,
            'sinopsis': 'Colección de cuentos que incluye "Casa tomada", uno de los relatos más famosos del autor.'
        }
    ]
    
    # Crear libros en la base de datos
    for libro_data in libros:
        libro, created = Libro.objects.get_or_create(
            isbn=libro_data['isbn'],
            defaults=libro_data
        )
        if created:
            print(f"Libro creado: {libro}")
    
    print(f"\n¡Datos creados exitosamente!")
    print(f"Autores creados: {Autor.objects.count()}")
    print(f"Libros creados: {Libro.objects.count()}")

if __name__ == '__main__':
    crear_datos_ejemplo()
