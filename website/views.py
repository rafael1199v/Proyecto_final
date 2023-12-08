from flask import Blueprint, render_template, session, redirect, url_for
from .models import *
views = Blueprint("views", __name__)

#Ruta principal
@views.route("/")
def home():

    #Revisamos si existe un usuario que haya iniciado sesion
    if 'user_id' not in session:
        return redirect(url_for("auth.login"))

    #Si existiera un usuario, obtenemos todos sus datos para luego mostrarlos
    usuario = Usuario.get_datos(session["user_id"])
    nombre, edad, ubicacion, telefono = usuario

    return render_template("home.html", nombre=nombre, edad=edad, ubicacion=ubicacion, telefono=telefono)


