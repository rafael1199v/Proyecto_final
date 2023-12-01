from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        print("Email =", email)
        print("Password =", password)
    
    return render_template("login.html")

@auth.route("/noticias")
def logout():
    return render_template("noticias.html")

@auth.route("/registro")
def sign_up():
    return render_template("registro.html")

@auth.route("/publicaciones")
def publicaciones():
    return render_template("publicaciones.html")

@auth.route("/mensajes")
def mensajes():
    return render_template("mensajes.html")