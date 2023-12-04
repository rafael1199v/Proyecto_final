from flask import Blueprint, render_template, session, redirect, url_for

views = Blueprint("views", __name__)

@views.route("/")
def home():
    if 'user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("home.html")


