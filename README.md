# Proyecto Final: UCB Social

Este proyecto es una red social que permite enviar mensajes, hacer amistades y ver publicaciones y noticias según sus temas.

### Objetivo
El objetivo de este proyecto es de explorar nuestros conocimientos en el lenguaje de programación Python y el manejo de bases de datos OracleDB en forma de un proyecto final para la universidad.

### Requisitos
Para utilizar esta aplicación se requiere el lenguaje de programación Python y las siguientes librerías:
- OracleDB
- Flask

Para instalar dichas librerías, usa los siguientes comandos:
```
pip install oracledb
pip install flask
```

### Modo de uso
Antes de empezar, requieres hacer un environment propio con las librerías mencionadas anteriormente.  
Posteriormente, para ejecutar el programa se debe ejecutar el archivo "main.py", que se encuentra en la raíz del proyecto. Una vez ahí se generará un link en la consola, dicho link se abre en su explorador preferido para entrar al proyecto, lo primero que debes hacer es iniciar sesión o registrarte. Luego de ello, puedes usar las demás funcionalidades de la red social, como el envío de mensajes, publicaciones o hacer amigos en la red.  
Las publicaciones cuentan con una diversa serie de opciones, tales como añadir a qué tema está relacionado, incluir hashtags, ajustar un nivel de importancia o convertir la publicación en noticia adjuntando fuentes sobre dicha noticia.

### Componentes del proyecto
* Perfil.html  
Es la ruta principal, donde el usuario puede ver su información básica como su nombre, ubicación, edad, etc.

* Login.html  
Es la primera ruta que el usuario verá, donde le pedirá el correo electrónico correspondiente más su contraseña. Sin embargo, si escribe mal alguna de estas dos peticiones se le notificará un error.

* Registro.html  
Es la página donde un nuevo usuario va a poder registrarse con sus diferentes datos personales como puede ser su nombre, ubicación 

* Publicaciones.html  
Es donde el usuario observa las distintas publicaciones que hacen los usuarios como las noticias o hashtags.

* Mensajes.html  
Es la ruta donde el usuario podrá ver los diferentes mensajes que le envían los demás usuarios.

* Main.py  
Es el archivo principal donde se corre la aplicación usando modularidad creando la app mediante una nueva función llamada create app.

* __init__.py  
Este archivo sirve para que python identifique que la carpeta que contiene el mismo  directorio de paquetes python y así importar los módulos que contiene la carpeta.

* data.py  
Este módulo es solo para la conexión de la base de datos de oracle con python, donde aparte de crear la conexion, se crear un cursor que servirá para la diferentes consultas realizadas por el usuario.

* models.py  
En este archivo se crearon todas las clases necesarias para el debido funcionamiento del programa tales como: Usuario, Mensajes, Credenciales.

* views.py  
Es el archivo que se encarga de organizar un grupo de vista de la aplicación, registrados con un blueprint. En esta misma se encuentra definida la ruta principal

* RED_DATABASE.sql  
En este archivo se encuentran los elementos necesarios para crear la base de datos necesaria para este programa, como ser: Tablas, llaves primarias, llaves foráneas y secuencias.

* Script Poblacion.sql  
Este archivo contiene scripts generados mediante Inteligencia Artificial para poblar las tablas, como requerimiento solicitado por el cliente.
