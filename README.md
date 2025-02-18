# Registro y Búsqueda de Productos

Este es un proyecto desarrollado con **Python** y **Django** para gestionar el registro y la búsqueda de productos en una base de datos. Incluye funcionalidades para agregar, actualizar, eliminar y buscar productos de manera eficiente. Además, se utiliza un **entorno virtual** para gestionar las dependencias del proyecto.

----------

## Características

-   Registro de nuevos productos con nombre, descripción, precio y cantidad.
-   Búsqueda de productos por nombre o descripción.
-   Listado de todos los productos registrados.
-   Actualización y eliminación de productos.
-   Interfaz amigable con Django Admin para la gestión de productos.

----------

## Tecnologías Utilizadas

-   **Python 3.x**
-   **Django 4.x**
-   **SQLite** (Base de datos por defecto)
-   **HTML/CSS** para el diseño de las plantillas.

----------

## Requisitos Previos

-   **Python** instalado en tu sistema. Verifica la instalación con:
		    
	    python --version
    
-   **Pip** (Administrador de paquetes de Python). Verifica con:
            
	    pip --version 
----------

## Instalación

### 1. Clonar el repositorio

	git clone https://github.com/G44T/django.git

	cd nombre-del-repositorio

### 2. Crear un entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto. Ejecuta el siguiente comando:

	python -m venv venv 

Para activar el entorno virtual:

-   En **Windows**:
        
	    env\Scripts\activate
    
-   En **macOS / Linux**:
        
	    source env/bin/activate 
    

Deberías ver `(env)` al inicio de la línea de comandos, indicando que el entorno virtual está activo.

### 3. Instalar dependencias

Instala las dependencias necesarias con:

	pip install -r requirements.txt

Si no tienes un archivo `requirements.txt`, puedes crearlo con:

	pip freeze > requirements.txt

----------

### 4. Configurar la base de datos

Ejecuta las migraciones de la base de datos:

	python manage.py makemigrations
	python manage.py migrate 

### 5. Crear un superusuario

Para acceder al panel de administración de Django, crea un superusuario:

	python manage.py createsuperuser

### 6. Iniciar el servidor de desarrollo

	python manage.py runserver 

Accede a la aplicación en tu navegador en: `http://127.0.0.1:8000`

----------

## Uso

-   **Página principal:** 
-   **Registrar Producto:** Formulario para agregar un nuevo producto.
-   **Buscar Producto:** Barra de búsqueda para encontrar productos por nombre o descripción.

----------

## Desactivando el entorno virtual

Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual con:

	deactivate	

----------

## Dependencias

Asegúrate de tener las siguientes dependencias en `requirements.txt`:

	Django>=3.12.6 

Si necesitas instalar otras dependencias, agrégalas en `requirements.txt` y ejecuta:

	pip install -r requirements.txt

----------

## Autor

-   **Tu Nombre** - [Alvarado Torres](https://github.com/G44T)