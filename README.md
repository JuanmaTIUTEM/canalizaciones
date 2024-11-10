# canalizaciones
Proyecto de clase de Django

Para ejecutar el código siga los siguientes pasos:
1. Generar, en cualquier espacio de su computadora, una carpeta para el proyecto y el entorno vitrual
2. Crear un entorno dentro de la carpeta:
   python -m venv nombre_del_entorno
3. Activar el entorno creado
   .\nombre_del_entorno\Scripts\activate
4. Instalar Django en el entorno virtual
   >:_pip install django
5. Clonar este repositorio
   >_:git clone https://github.com/JuanmaTIUTEM/canalizaciones.git
6. Ejecutar proyecto:
   6.1. Acceder a carpeta canalizaciones
        cd canalizaciones
   6.2. Ejecutar instruccion para iniciar servidor y proyecto
        python manage.py runserver
7. Si no hay ningun detalle, crear una rama con su  numero de control
   git pull origin main
   git checkout -b numero_de_control 
      Este comando hace dos cosas:
        a. Crea una nueva rama que tendra como nombre numero_de_control (donde este dato se sustituirá por su número de control).
        b. Cambia a esa rama.
8. Buscar el archivo home.html y modificar con sus datos de estudiante
9. Añadir los archivos modificados
   git add .
   git commit -m "Cambio de nombre en portada"
10. Subir la nueva rama al repositorio remoto
    git push origin numero_de_control
11.  Verificar en GitHub.Después de ejecutar git push, tu nueva rama debería aparecer en el repositorio en GitHub. Puedes verificar esto accediendo al repositorio en GitHub y seleccionando la lista de ramas para asegurarte de que la nueva rama esté disponible.
   
