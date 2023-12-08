import oracledb

#Se crea la conexion principal para la aplicación
try:
    connection_principal = oracledb.connect(user='PROYECTO_FINAL', password='PROYECTO_FINAL', dsn='LAPTOP-LBCR930N/xe')
    print("Tenemos conexion")
except:
    print("Hubo un error al crear la conexion")


#Se crea el cursor global para la aplicación
try:
    cursor = connection_principal.cursor()
    print("Se creo que cursor")
except:
    print("Hubo un error al crear el cursor")

