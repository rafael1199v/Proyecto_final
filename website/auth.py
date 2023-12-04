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
            return redirect(url_for("auth.perfil"))
        
        else:
            flash("Credenciales incorrectos", category="error")
    
    return render_template("login.html")

@auth.route("/noticias")
def noticias():
    return render_template("noticias.html")

@auth.route("/perfil")
def perfil():
    if "user_id" in session:
        return render_template("home.html")
    
    return redirect(url_for("auth.login"))


@auth.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect(url_for("auth.login"))

@auth.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        email = request.form.get('email')
        nombre_usuario = request.form("nombre_usuario")
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")
        ubicacion = request.form.get("ubicacion")
        telefono = request.form.get("telefono")
        contraseha = request.form.get("contrasenha")
        confirmarContrasenha = request.form.get("confContrasenha")

        if contraseha != confirmarContrasenha:
            flash("Las contraseñas no coinciden", category='error')
        elif len(email) < 5:
            flash("Introduce un email de mas de 4 caracteres", category='error')
        elif int(edad) < 10:
            flash("El usuario tiene que tener una edad mayor o igual a 10 años", category='error')
        else:
            flash("Cuenta creada exitosamente", category='success')
            pass

    return render_template("registro.html")

@auth.route("/publicaciones")
def publicaciones():
    return render_template("publicaciones.html")

@auth.route("/mensajes")
def mensajes():

    cursor.execute("""
                    select m.contenido, u.nombre
                    from mensaje m, usuario u
                    where m.id_usuario_receptor = u.id
                   """)
        
    filas = cursor.fetchall()
    return render_template("mensajes.html", filas=filas)