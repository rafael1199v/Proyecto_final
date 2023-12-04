from website import create_app
from website.data import connection, cursor

app = create_app()
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

if __name__ == "__main__":

    app.run(debug=True)

    cursor.close()
    connection.close()
