from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from .data import cursor
from .models import *
from datetime import datetime

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email: str = request.form.get('email')
        password: str = request.form.get('password')

        credenciales_usuario: tuple = Credenciales.get_credenciales(email, password)

        #Verificamos la existencia del usuario en la base de datos
        if credenciales_usuario:
            session.clear()
            session["user_id"] = credenciales_usuario[0]
            session["user_email"] = email

            flash("Sesion iniciada correctamente" ,category='success')
            return redirect(url_for("views.home"))
        
        else:
            flash("Credenciales incorrectos", category="error")
    
    return render_template("login.html")

@auth.route("/cerrar_sesion", methods=["GET"])
def cerrar_sesion():
    #Borramos los datos de session
    session.clear()
    return redirect(url_for("auth.login"))

@auth.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        email: str = request.form.get('email')
        nombre_usuario: str = request.form.get("nombre_usuario")
        nombre: str = request.form.get("nombre")
        edad: int = int(request.form.get("edad"))
        ubicacion: str = request.form.get("ubicacion")
        telefono: str = request.form.get("telefono")
        contrasenha: str = request.form.get("contrasenha")
        confirmarContrasenha: str = request.form.get("confContrasenha")

        #Verificamos los input del nuevo usuario

        if contrasenha != confirmarContrasenha:
            flash("Las contraseñas no coinciden", category='error')
        elif len(email) < 5:
            flash("Introduce un email de mas de 4 caracteres", category='error')
        elif edad < 10:
            flash("El usuario tiene que tener una edad mayor o igual a 10 años", category='error')
        elif len(nombre_usuario) < 4:
            flash("Se necesita un nombre de usuario mas largo", category='error')
        elif len(telefono) != 8:
            flash("Introduzca un numero de telefono valido", category='error')
        else:

            credeciales_usuario: tuple = Credenciales.verificar_nuevo_usuario(email)

            #Verficamos si las credenciales escritas por el nuevo usuario no estan siendo usadas
            if not credeciales_usuario:
                Credenciales.add_credenciales(nombre_usuario, email, contrasenha)
                Usuario.add_usuario(nombre, edad, ubicacion, telefono)
                flash("Cuenta creada exitosamente", category='success')

            else:
                flash("Cuenta Existente, intente otras credenciales", category="error")
            

    return render_template("registro.html")

@auth.route("/publicaciones")
def publicaciones():
    #Mediante estas funciones, conseguimos las noticias y hashtags de la base de datos
    noticias: list[tuple] = get_noticias()
    hashtags: list[tuple] = get_hashtags()

    return render_template("publicaciones.html", noticias=noticias, hashtags=hashtags)

@auth.route("/mensajes")
def mensajes():

    #Conseguimos todos los usuarios que son amigos del usuario actual
    usuario_receptor: int = session["user_id"]
    mensajes_usuario: tuple = Mensaje.get_mensajes(usuario_receptor)
    
    return render_template("mensajes.html", mensajes_usuario=mensajes_usuario)


@auth.route("/enviar", methods=["GET", "POST"])
def enviar():

    #Verificamos si algun usuario a iniciado sesion
    if "user_id" not in session:
       return redirect(url_for("login.html"))
    
    if request.method == "POST":
        destinatario: str = request.form.get("correos")
        contenido: str = request.form.get("mensaje")
        
        #Verificamos el contenido del mensaje antes de actualizar la base de datos
        if len(contenido) > 200:
            flash("El contendo del mensaje excede los 200 caracteres" ,category="error")
        elif len(contenido) == 0:
            flash("La caja de texto esta vacia", category="error")
        else:
            id_usuario_receptor: int = Mensaje.get_usuario_receptor(destinatario)
            id_usuario_emisor: int = session["user_id"]
    
            Mensaje.add_mensaje(contenido, id_usuario_emisor, id_usuario_receptor)
            flash("Mensaje enviado correctamente", category="success")

    #Conseguimos las personas a las cuales le podemos enviar un mensaje
    usuario_emisor: int = session["user_id"]
    personas: tuple = Mensaje.get_personas(usuario_emisor)
    return render_template("enviar.html", personas = personas)

@auth.route("/amigos", methods=["GET", "POST"])
def amigos():

    #Verificamos si algun usuario a iniciado sesion
    if "user_id" not in session:
       return redirect(url_for("auth.login"))
    

    #Obtenemos el id de la sesion actual
    id_usuario: int = session["user_id"]

    if request.method == "POST":
        nuevo_amigo: str = request.form.get("nuevo_amigo")
        print("correo del nuevo amigo", nuevo_amigo)
        #Obtenemos el identificador del nuevo amigo que queremos agregar y luego lo agregamos a la base de datos
        id_usuario_amigo: int = Usuario.get_id_nuevo_amigo(nuevo_amigo)
        Usuario.add_amigo(id_usuario, id_usuario_amigo)
        print("Amigo agregado")

    #Conseguimos los datos de las personas que son amigo del usuario actual y las personas que todavia no son amigo del usuario actual
    amigos: tuple = Usuario.get_amigos(id_usuario)
    numero_amigos: int = len(amigos)
    posibles_amigos: tuple = Usuario.get_nuevas_personas(id_usuario)
    fecha_amigos = [amigo[1].date() for amigo in amigos]
    
    return render_template("amigos.html", amigos=amigos, numero_amigos=numero_amigos, posibles_amigos=posibles_amigos, fecha_amigos=fecha_amigos)