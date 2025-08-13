# Sistema de Gestión de Libros

Una aplicación web desarrollada en Django para gestionar una biblioteca de libros y autores.

## Características

- **Gestión de Libros**: Agregar, listar y eliminar libros
- **Gestión de Autores**: Agregar, listar y eliminar autores
- **Búsqueda**: Buscar libros por título, autor o género
- **Búsqueda de Autores**: Buscar por nombre, apellido o nacionalidad
- **Formularios Inteligentes**: Los datos se mantienen al usar el botón atrás
- **Confirmación de Eliminación**: Páginas de confirmación antes de eliminar
- **Validaciones**: No se pueden eliminar autores con libros asociados
- **Diseño Responsivo**: Interfaz moderna con Bootstrap

## Tecnologías Utilizadas

- **Backend**: Django 4.2.7
- **Base de Datos**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Control de Versiones**: Git

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/TuPrimeraPagina-Bea.git
   cd TuPrimeraPagina-Bea
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Poblar la base de datos con datos de ejemplo**
   ```bash
   python populate_db.py
   ```

7. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

8. **Abrir en el navegador**
   ```
   http://127.0.0.1:8000/
   ```

## 📖 Uso

### Página Principal
- Accede a la página principal en `http://127.0.0.1:8000/`
- Navega por las diferentes secciones usando los botones

### Gestión de Libros
- **Ver libros**: `/libros/`
- **Agregar libro**: `/libros/crear/`
- **Eliminar libro**: Haz clic en "Eliminar" en cualquier tarjeta de libro

### Gestión de Autores
- **Ver autores**: `/autores/`
- **Agregar autor**: `/autores/crear/`
- **Eliminar autor**: Haz clic en "Eliminar" en cualquier tarjeta de autor

### Búsqueda
- Usa la barra de búsqueda en las páginas de listado
- Busca por título, autor o género en libros
- Busca por nombre, apellido o nacionalidad en autores

## Estructura del Proyecto

```
TuPrimeraPagina-Bea/
├── mi_app/                    # Aplicación principal
│   ├── models.py             # Modelos de datos
│   ├── views.py              # Vistas de la aplicación
│   ├── forms.py              # Formularios
│   ├── urls.py               # URLs de la aplicación
│   ├── admin.py              # Configuración del admin
│   └── templates/            # Plantillas HTML
│       ├── base.html         # Plantilla base
│       ├── index.html        # Página principal
│       └── mi_app/           # Plantillas específicas
├── mi_proyecto/              # Configuración del proyecto
│   ├── settings.py           # Configuración de Django
│   ├── urls.py               # URLs principales
│   └── wsgi.py               # Configuración WSGI
├── static/                   # Archivos estáticos
├── manage.py                 # Script de gestión de Django
├── requirements.txt          # Dependencias del proyecto
├── populate_db.py            # Script para datos de ejemplo
└── README.md                 # Este archivo
```

## Modelos de Datos

### Autor
- `nombre`: Nombre del autor
- `apellido`: Apellido del autor
- `nacionalidad`: Nacionalidad del autor
- `fecha_nacimiento`: Fecha de nacimiento
- `biografia`: Biografía (opcional)

### Libro
- `titulo`: Título del libro
- `autor`: Relación con el modelo Autor
- `genero`: Género literario
- `fecha_publicacion`: Fecha de publicación
- `isbn`: Número ISBN único (Número identificador de un libro)
- `precio`: Precio del libro
- `sinopsis`: Sinopsis del libro

## Características de Seguridad

- **Validación de formularios**: Todos los formularios están validados
- **Confirmación de eliminación**: Páginas de confirmación antes de eliminar
- **Validación de relaciones**: No se pueden eliminar autores con libros asociados

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

Desarrollado como proyecto de aprendizaje de Django.
