from .data import cursor, connection
from datetime import datetime, timedelta
import random

class Credenciales():
    def __init__(self, id: int, nombre_usuario: str, correo: str, contrasenha: str) -> None:
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasenha = contrasenha


    def get_nombre(self) -> str:
        return self.nombre_usuario
    
    def get_correo(self) -> str:
        return self.correo
    
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre_usuario = nuevo_nombre

    def set_correo(self, nuevo_correo: str) -> None:
        self.correo = nuevo_correo


    def get_credenciales(correo: str, contrasenha: str) -> tuple:
        cursor.execute("SELECT * FROM CREDENCIALES WHERE CORREO = :CORREO AND CONTRASENHA = :CONTRASENHA", {'CORREO': correo, 'CONTRASENHA': contrasenha})
        fila = cursor.fetchone()
        return fila
    
    def verificar_nuevo_usuario(correo: str) -> tuple:
        cursor.execute("SELECT CORREO FROM CREDENCIALES WHERE CORREO = :CORREO", {'CORREO': correo})
        correo_existente = cursor.fetchone()
        return correo_existente
    

    def add_credenciales(nombre_usuario: str, correo: str, contrasenha: str) -> None:
        try:
            cursor.execute("INSERT INTO CREDENCIALES (ID, NOMBRE_USUARIO, CORREO, CONTRASENHA) VALUES(CREDENCIALES_SEQ.NEXTVAL, :NOMBRE_C, :CORREO_C, :CONTRASENHA_C)", 
                        {'NOMBRE_C': nombre_usuario, 'CORREO_C': correo, 'CONTRASENHA_C': contrasenha})
            
            connection.commit()
        except:

            print("No se pudo crear el nuevo usuario 1")
        


class Usuario(Credenciales):
    def __init__(self, id, nombre: str, edad: int, ubicacion: str, telefono: str, id_credenciales: int) -> None:
        super().__init__(id_credenciales)

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.id_credenciales = id_credenciales


    def get_datos(id_credenciales) -> tuple:
        cursor.execute("SELECT * FROM USUARIO WHERE ID_CREDENCIALES = :id_c", {'id_c': id_credenciales})
        fila = cursor.fetchone()
        return fila
    

    def add_usuario(nombre: str, edad: int, ubicacion: str, telefono: str) -> None:
        try:
            cursor.execute("INSERT INTO USUARIO (ID, NOMBRE, EDAD, UBICACION, TELEFONO, ID_CREDENCIALES) VALUES(USUARIO_SEQ.NEXTVAL, :NOMBRE_U, :EDAD_U, :UBICACION_U, :TELEFONO_U, USUARIO_SEQ.CURRVAL)", 
                        {'NOMBRE_U': nombre, 'EDAD_U': edad, 'UBICACION_U': ubicacion, 'TELEFONO_U': telefono})
            
            connection.commit()
        except:

            print("No se pudo crear el nuevo usuario 2")

    def get_amigos(id_usuario: int) -> tuple:
        cursor.execute("SELECT DISTINCT U.NOMBRE, A.FECHA_AMISTAD FROM USUARIO U, USUARIO_AMIGO A WHERE U.ID IN (SELECT ID_AMIGO FROM USUARIO_AMIGO WHERE ID_USUARIO = :ID_U) AND U.ID = A.ID_AMIGO AND A.ID_USUARIO = :ID_U",
                       {'ID_U': id_usuario})
        filas = cursor.fetchall()
        return filas
    
    def get_nuevas_personas(id_usuario: int) -> tuple:
        cursor.execute("SELECT C.CORREO FROM USUARIO U, CREDENCIALES C WHERE U.ID NOT IN (SELECT ID_AMIGO FROM USUARIO_AMIGO WHERE ID_USUARIO = :ID_U) AND U.ID_CREDENCIALES = C.ID AND U.ID <> :ID_U",
                       {'ID_U': id_usuario})
        
        filas = cursor.fetchall()
        return filas
    
    def get_id_nuevo_amigo(correo_amigo: str) -> int:
        cursor.execute("SELECT ID FROM CREDENCIALES WHERE CORREO = :CORREO_AMIGO", {'CORREO_AMIGO': correo_amigo})
        id_usuario_amigo = cursor.fetchone()
        return int(id_usuario_amigo[0])
    
    def add_amigo(id_usuario: str, id_usuario_amigo) -> None:
        try:
            fecha_actual = datetime.now()

        
            fecha_amistad = fecha_actual - timedelta(days=random.randint(1, 365))

        
            fecha_amistad_str = fecha_amistad.strftime('%Y-%m-%d %H:%M:%S')


            cursor.execute("INSERT INTO USUARIO_AMIGO (ID, ID_USUARIO, ID_AMIGO, FECHA_AMISTAD) VALUES (USUARIO_AMIGO_SEQ.NEXTVAL, :ID_USUARIO_U, :ID_AMIGO_U, TO_DATE(:FECHA_AMISTAD, 'YYYY-MM-DD HH24:MI:SS'))",
                       {'ID_USUARIO_U': id_usuario, 'ID_AMIGO_U': id_usuario_amigo, 'FECHA_AMISTAD': fecha_amistad_str})
            
            connection.commit()
            
            cursor.execute("INSERT INTO USUARIO_AMIGO (ID, ID_USUARIO, ID_AMIGO, FECHA_AMISTAD) VALUES (USUARIO_AMIGO_SEQ.NEXTVAL, :ID_USUARIO_U, :ID_AMIGO_U, TO_DATE(:FECHA_AMISTAD, 'YYYY-MM-DD HH24:MI:SS'))",
                       {'ID_USUARIO_U': id_usuario_amigo, 'ID_AMIGO_U': id_usuario, 'FECHA_AMISTAD': fecha_amistad_str})
            
            connection.commit()
        except:

            print("No se pudo agreagar al amigo")

        
        


class TipoPublicacion():
    def __init__(self, id: int, tema_publicacion: str, tipo_publicacion: str) -> None:
        self.id = id
        self.tema_publicacion = tema_publicacion
        self.tipo_publicacion = tipo_publicacion


class Mensaje(Usuario):

    def __init__(self, id: int, contenido: str, fecha_publicacion: str, id_usuario_emisor: int, id_usuario_receptor: int) -> None:
        super().__init__(id_usuario_emisor, id_usuario_receptor)

        self.id = id
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion

    def get_mensajes(id_usuario_receptor) -> tuple:
        cursor.execute("SELECT M.CONTENIDO, U.NOMBRE FROM MENSAJE M, USUARIO U WHERE M.ID_USUARIO_EMISOR = U.ID AND M.ID_USUARIO_RECEPTOR = :ID_R", {'ID_R': id_usuario_receptor})
        filas = cursor.fetchall()

        return filas
    
    def get_personas(id_usuario_emisor) -> tuple:
        cursor.execute("SELECT CORREO FROM CREDENCIALES WHERE ID <> :ID_E", {'ID_E': id_usuario_emisor})
        filas = cursor.fetchall()
        return filas
    
    def get_usuario_receptor(correo: str) -> int:
        cursor.execute("SELECT ID FROM CREDENCIALES WHERE CORREO = :CORREO", {'CORREO': correo})
        usuario_receptor = cursor.fetchone()
        return int(usuario_receptor[0])
    
    def add_mensaje(contenido: str, id_usuario_emisor: int, id_usuario_receptor: int) -> None:


        try:
            cursor.execute("INSERT INTO MENSAJE (ID, CONTENIDO, ID_USUARIO_EMISOR, ID_USUARIO_RECEPTOR) VALUES (MENSAJE_SEQ.NEXTVAL, :CONTENIDO_U, :EMISOR_U, :RECEPTOR_U)",
                       {'CONTENIDO_U': contenido, 'EMISOR_U': id_usuario_emisor, 'RECEPTOR_U': id_usuario_receptor})
            
            connection.commit()
        except:

            print("No se pudo enviar el mensaje")
        
        

    
    def get_personas(id_usuario_emisor) -> tuple:
        cursor.execute("SELECT CORREO FROM CREDENCIALES WHERE ID <> :ID_E", {'ID_E': id_usuario_emisor})
        filas = cursor.fetchall()
        return filas
    
    def get_usuario_receptor(correo: str) -> int:
        cursor.execute("SELECT ID FROM CREDENCIALES WHERE CORREO = :CORREO", {'CORREO': correo})
        usuario_receptor = cursor.fetchone()
        return int(usuario_receptor[0])
    
    def add_mensaje(contenido: str, id_usuario_emisor: int, id_usuario_receptor: int) -> None:


        try:
            cursor.execute("INSERT INTO MENSAJE (ID, CONTENIDO, ID_USUARIO_EMISOR, ID_USUARIO_RECEPTOR) VALUES (MENSAJE_SEQ.NEXTVAL, :CONTENIDO_U, :EMISOR_U, :RECEPTOR_U)",
                       {'CONTENIDO_U': contenido, 'EMISOR_U': id_usuario_emisor, 'RECEPTOR_U': id_usuario_receptor})
            
            connection.commit()
        except:

            print("No se pudo enviar el mensaje")
       
