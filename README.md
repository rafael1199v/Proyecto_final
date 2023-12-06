# Proyecto Final: UCB Social

El objetivo de este proyecto es tratar de simular una red social con sus funcionalidades básicas, como la de tener amigos, ver publicaciones o ver mensajes.

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
Para ejecutar el programa se debe ejecutar el archivo "main.py", que se encuentra en la raíz del proyecto. Una vez ahí se abrirá tu navegador principal, lo primero que debes hacer es iniciar sesión o registrarte. Luego de ello, puedes usar las demás funcionalidades de la red social, como el envío de mensajes, publicaciones o hacer amigos en la red.

Las publicaciones cuentan con una diversa serie de opciones, tales como añadir a qué tema está relacionado, incluir hashtags, ajustar un nivel de importancia o convertir la publicación en noticia adjuntando fuentes sobre dicha noticia.

### Modulos
* \__init__.py
	Este archivo sirve para que python identifique que la carpeta que contiene el mismo 
	directorio de paquetes python y así importar los módulos que contiene la carpeta.

* data.py
	Este módulo es solo para la conexión de la base de datos de oracle con python, donde
	aparte de crear la conexion, se crear un cursor que servirá para la diferentes consultas
  realizadas por el usuario.

* models.py
	En este archivo se crearon todas las clases necesarias para el debido funcionamiento	del programa tales como: Usuario, Mensajes, Credenciales.

* views.py
  Es el archivo que se encarga de organizar un grupo de vista de la aplicación, registrados con un blueprint. En esta misma se encuentra definida la ruta principal
