# Cursos Marciales - Tien Long Hu

## Descripción del Proyecto

Este es un proyecto desarrollado como parte del trabajo de nivel intermedio de la Diplomatura en Django, titulado **"Aplicaciones"**. El objetivo principal de este proyecto es proporcionar una plataforma en línea para la gestión de cursos marciales, donde los usuarios pueden visualizar, inscribirse y gestionar sus cursos de manera eficiente.

## Funcionalidades

- **Registro de Usuarios**: Los usuarios pueden registrarse en la plataforma, creando una cuenta con información personal.
- **Autenticación**: Sistema de inicio de sesión para acceder a la plataforma.
- **Administración de Cursos**: Los administradores pueden crear, modificar y eliminar cursos a través de la interfaz de administración de Django.
- **Visualización de Cursos**: Los usuarios pueden explorar diferentes cursos marciales disponibles, con detalles como nombre, descripción, profesor, precio, entre otros.
- **Inscripción en Cursos**: Los usuarios pueden inscribirse en los cursos de su interés y gestionar su inscripción.
- **Gestión de Imágenes**: Cada curso puede tener una imagen asociada para mejorar la presentación visual.

## Tecnologías Utilizadas

- **Django**: Framework web de alto nivel para el desarrollo del backend.
- **Python**: Lenguaje de programación utilizado para el desarrollo del proyecto.
- **SQLite**: Base de datos utilizada para el almacenamiento de datos (configurable a otras bases de datos como PostgreSQL).
- **HTML/CSS**: Para la creación de la interfaz de usuario.
- **Bootstrap**: Framework CSS utilizado para el diseño responsivo.
- **Admin de Django**: Interfaz de administración incorporada para gestionar usuarios y cursos.

CAPTURAS DEL PROYECTO:

<img src="https://github.com/eliasescalante/CursosMarciales_UTN/blob/master/media/captura.png" width="600" />

## Estructura del Proyecto

```plaintext
CursosMarciales/
├── manage.py
├── contacto/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   └── views.py
├── usuarios/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   └── views.py
├── static/
│   ├──academia/
│   ├──contacto/
│   ├──cursos/
│   └── usuarios/
├── media/
│   ├──academia/
│       ├──css/
│       └── js/
├── CursosMarciales/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── cursos/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   └── views.py
├── academia/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   └── views.py
└── templates/
    |__ admin/
    ├── cursos/
    ├── usuarios/
    ├── academia/
    └── contacto/