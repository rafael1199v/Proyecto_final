from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from .data import cursor
from .models import *


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        credenciales_usuario = Credenciales.get_credenciales(email, password)
        
        if credenciales_usuario:

            session["user_id"] = credenciales_usuario[0]
            session["user_email"] = email

            flash("Sesion iniciada correctamente" ,category='success')
            return redirect(url_for("views.home"))
        
        else:
            flash("Credenciales incorrectos", category="error")
    
    return render_template("login.html")

@auth.route("/noticias")
def noticias():
    return render_template("noticias.html")


@auth.route("/cerrar_sesion", methods=["GET"])
def cerrar_sesion():
    session.clear()
    return redirect(url_for("auth.login"))

@auth.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        email = request.form.get('email')
        nombre_usuario = request.form.get("nombre_usuario")
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        ubicacion = request.form.get("ubicacion")
        telefono = request.form.get("telefono")
        contrasenha = request.form.get("contrasenha")
        confirmarContrasenha = request.form.get("confContrasenha")

        if contrasenha != confirmarContrasenha:
            flash("Las contraseñas no coinciden", category='error')
        elif len(email) < 5:
            flash("Introduce un email de mas de 4 caracteres", category='error')
        elif edad < 10:
            flash("El usuario tiene que tener una edad mayor o igual a 10 años", category='error')
        else:

            credeciales_usuario = Credenciales.verificar_nuevo_usuario(email)

            if not credeciales_usuario:
                Credenciales.add_credenciales(nombre_usuario, email, contrasenha)
                Usuario.add_usuario(nombre, edad, ubicacion, telefono)
                flash("Cuenta creada exitosamente", category='success')

            else:
                flash("Cuenta Existente, intente otras credenciales", category="error")
            

    return render_template("registro.html")

@auth.route("/publicaciones")
def publicaciones():
    return render_template("publicaciones.html")

@auth.route("/mensajes")
def mensajes():

    usuario_receptor = session["user_id"]

    mensajes_usuario = Mensaje.get_mensajes(usuario_receptor)
    
    
    return render_template("mensajes.html", mensajes_usuario=mensajes_usuario)


@auth.route("/enviar", methods=["GET", "POST"])
def enviar():

    if "user_id" not in session:
       return redirect(url_for("login.html"))
    

    if request.method == "POST":
        destinatario = request.form.get("correos")
        contenido = request.form.get("mensaje")
        
        print(destinatario)
        print(contenido)

        id_usuario_receptor = Mensaje.get_usuario_receptor(destinatario)
        id_usuario_emisor = int(session["user_id"])
    
        Mensaje.add_mensaje(contenido, id_usuario_emisor, id_usuario_receptor)
        
    usuario_emisor = session["user_id"]
    personas = Mensaje.get_personas(usuario_emisor)
    return render_template("enviar.html", personas = personas)
    