# Cursos Marciales - Tien Long Hu

## Descripción del Proyecto

Este es un proyecto desarrollado como parte del trabajo de nivel intermedio de la Diplomatura en Django, titulado **"Aplicaciones"**. El objetivo principal de este proyecto es proporcionar una plataforma en línea para la gestión de cursos marciales, donde los usuarios pueden visualizar, inscribirse y gestionar sus cursos de manera eficiente. Este proyecto tiene aplicacion real porque fue solicitado por la escuela Tien Long Hu de Quilmes a cargo del maestro Ruben Braun el cual considera una buena opcion para promocionar y vender sus cursos dentro de la escuela y captar mas alumnos para aquellos alumnos que deseen avanzar dentro de la escuela.

## Funcionalidades

- **Registro de Usuarios**: Los usuarios pueden registrarse en la plataforma, creando una cuenta con información personal. (al crear un usuario se les asocia un perfil de usuario)
- **Login**: Los usuarios pueden logearse con su cuenta, ver su perfil, agregar o eliminar o cambiar su imagen de avatar ademas de modificar toda su informacion del perfil.
- **Autenticación**: Sistema de inicio de sesión para acceder a la plataforma.
- **Administración de Cursos**: Los administradores pueden crear, modificar y eliminar cursos a través de la interfaz de administración de Django.
- **Visualización de Cursos**: Los usuarios pueden explorar diferentes cursos marciales disponibles, con detalles como nombre, descripción, profesor, precio, entre otros.
- **Inscripción en Cursos**: Los usuarios pueden inscribirse en los cursos de su interés y gestionar su inscripción, obteniendo un ticket de compra al suscribirse.
- **Mis Cursos**: Al inscribirse al curso, el mismo reduce el cupo y se registra en los cursos del usuario logeado y este no puede volver a inscribirse en el mismo curso a menos que se desuscriban al mismo.
- **Noticias**: Los administradores pueden publicar noticias y los usuarios pueden visualizarlas. Los Administradores pueden hacerlo desde la vista de Admin de Django.

## Tecnologías Utilizadas

- **Django**: Framework web de alto nivel para el desarrollo del backend.
- **Python**: Lenguaje de programación utilizado para el desarrollo del proyecto.
- **SQLite**: Base de datos utilizada para el almacenamiento de datos.
- **HTML/CSS**: Para la creación de la interfaz de usuario.
- **Bootstrap**: Framework CSS utilizado para el diseño responsivo.
- **Admin de Django**: Interfaz de administración incorporada para gestionar usuarios y cursos.
- **Green Sock**: Se utilizo la libreria GASP para agregar animaciones al scrollear la seccion de noticias.
- **JavaScript**: Se utilizo AJAX para no bloquear el flujo de la pagina.
- **Rest_framework** Para generar una Rest-Api. 
- **SITEMAP** sitemap.xml
- **SERVICIO DE PAGOS** mercado pago.

CAPTURAS DEL PROYECTO:

<img src="https://github.com/eliasescalante/CursosMarciales_UTN/blob/master/media/captura.png" width="900" />
<img src="https://github.com/eliasescalante/CursosMarciales_UTN/blob/master/media/captura2.png" width="900"/>
<img src="https://github.com/eliasescalante/CursosMarciales_UTN/blob/master/media/captura_api.png" width="900" />
