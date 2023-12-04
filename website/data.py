import oracledb

try:
    connection = oracledb.connect(user='PROYECTO_FINAL', password='PROYECTO_FINAL', dsn='LAPTOP-LBCR930N/xe')
    print("Tenemos conexion")
except:
    print("Por alguna razon no se pudo")


try:
    cursor = connection.cursor()
    print("Se creo que cursor")
except:
    print("No se pudo crear el cursor")

