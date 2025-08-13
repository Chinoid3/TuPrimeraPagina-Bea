from django.db import models
from django.urls import reverse

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def get_absolute_url(self):
        return reverse('autor_list')
    
    class Meta:
        verbose_name_plural = "Autores"

class Libro(models.Model):
    GENEROS = [
        ('ficcion', 'Ficción'),
        ('no_ficcion', 'No Ficción'),
        ('fantasia', 'Fantasía'),
        ('misterio', 'Misterio'),
        ('romance', 'Romance'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('biografia', 'Biografía'),
        ('historia', 'Historia'),
    ]
    
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    genero = models.CharField(max_length=20, choices=GENEROS)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    sinopsis = models.TextField()
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('libro_list')