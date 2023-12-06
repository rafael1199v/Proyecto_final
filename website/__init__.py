from flask import Flask

#Crea los prefijos de rutas principales para el funcionamiento para la aplicacion
def create_app():
    app = Flask(__name__)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app