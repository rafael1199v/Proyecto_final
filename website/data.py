import oracledb

#Se crea la conexion principal para la aplicación
try:
    connection_principal = oracledb.connect(user='PROYECTO_FINAL', password='PROYECTO_FINAL', dsn='LAPTOP-LBCR930N/xe')
    print("Tenemos conexion")
except:
    print("Por alguna razon no se pudo")


#Se crea el cursor global para la aplicación
try:
    cursor = connection_principal.cursor()
    print("Se creo que cursor")
except:
    print("No se pudo crear el cursor")

