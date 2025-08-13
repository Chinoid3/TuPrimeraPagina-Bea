from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.libro_list, name='libro_list'),
    path('libros/crear/', views.libro_create, name='libro_create'),
    path('libros/<int:libro_id>/eliminar/', views.libro_delete, name='libro_delete'),
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/crear/', views.autor_create, name='autor_create'),
    path('autores/<int:autor_id>/eliminar/', views.autor_delete, name='autor_delete'),
]