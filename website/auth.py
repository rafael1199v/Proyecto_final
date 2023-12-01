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

@auth.route("/logout")
def logout():
    return "<h1> Hola </h1>"

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")