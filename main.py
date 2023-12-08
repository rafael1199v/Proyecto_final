from website import create_app
from website.data import connection_principal, cursor

#Creacion de la app
app = create_app()
app.config['SECRET_KEY'] = 'super_clave_secreta'

if __name__ == "__main__":

    try:
        app.run(debug=False)
    finally:

        cursor.close()
        connection_principal.close()
