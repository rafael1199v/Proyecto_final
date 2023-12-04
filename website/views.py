from flask import Blueprint, render_template, session, redirect, url_for
from .models import *
views = Blueprint("views", __name__)

@views.route("/")
def home():
    if 'user_id' not in session:
        return redirect(url_for("auth.login"))
    
    usuario = Usuario.get_datos(session["user_id"])

    id, nombre, edad, ubicacion, telefono, id_credenciales = usuario

    
    return render_template("home.html", nombre=nombre, edad=edad, ubicacion=ubicacion, telefono=telefono)


