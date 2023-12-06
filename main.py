from website import create_app
from website.data import connection, cursor


app = create_app()
app.config['SECRET_KEY'] = 'super_clave_secreta'

if __name__ == "__main__":

    try:
        app.run(debug=True)
    finally:

        cursor.close()
        connection.close()
