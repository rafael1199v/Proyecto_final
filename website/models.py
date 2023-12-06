from .data import cursor, connection
from datetime import datetime

class Credenciales():
    """La clase Credenciales representa las credenciales de un usuario en una aplicacion
    """
    def __init__(self, id: int, nombre_usuario: str, correo: str, contrasenha: str) -> None:

        """Este metodo inicializa un objeto Credenciales
        Args:
            id(int)
            nombre_usuario(str)
            correo(str)
            contrasenha(str)

        Atributos:
            id(int): Identificador unico
            nombre_usuario(str): Nombre del usuario
            correo(str): Correo del usuario
            contrasenha(str): Contraseña del usuario
        """
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasenha = contrasenha

    def get_correo(self) -> str:
        """Esta funcion retorna el correo de un usuario

        Args: Ninguno

        Retorna:
            str: El correo del usuario
        """
        return self.correo
    
    def get_credenciales(correo: str, contrasenha: str) -> tuple:
        """Este metodo devuelve las credenciales en forma de tupla

        Args:
            correo(str): Correo del usuario
            contrasenha: Contraseña del usuario
        
        Retorna:
            list[tuple]: Las credenciales del usuario
        """
        cursor.execute("SELECT * FROM CREDENCIALES WHERE CORREO = :CORREO AND CONTRASENHA = :CONTRASENHA", {'CORREO': correo, 'CONTRASENHA': contrasenha})
        fila = cursor.fetchone()
        return fila
    
    def verificar_nuevo_usuario(correo: str) -> tuple:
        """Este metodo retorna una tupla vacia o no con la intencion de verifica si existe un usuario en la base de datos

        Args:
            correo(str): Correo de las credenciales del usuario

        Retorna:
            list[tuple]: El primer dato extraido de la consulta, verificando si existe o no el usuario en la basde datos
        """

        cursor.execute("SELECT CORREO FROM CREDENCIALES WHERE CORREO = :CORREO", {'CORREO': correo})
        correo_existente = cursor.fetchone()
        return correo_existente
    

    def add_credenciales(nombre_usuario: str, correo: str, contrasenha: str) -> None:
        """Este metodo añade credenciales nuevas a la base de datos

        Args:
            nombre_usuario(str): Nombre del usuario
            correo(str): Correo del usuario
            contrasenha: Contraseña del usuario

        Retorno: Ninguno
        """
        try:
            cursor.execute("INSERT INTO CREDENCIALES (ID, NOMBRE_USUARIO, CORREO, CONTRASENHA) VALUES(CREDENCIALES_SEQ.NEXTVAL, :NOMBRE_C, :CORREO_C, :CONTRASENHA_C)", 
                        {'NOMBRE_C': nombre_usuario, 'CORREO_C': correo, 'CONTRASENHA_C': contrasenha})
            
            connection.commit()
        except:
            connection.rollback()
            print("No se pudo crear el nuevo usuario 1")
        


class Usuario(Credenciales):
    """La clase usuario representa a un usuario de una aplicacion en la vida real
    """
    def __init__(self, id, nombre: str, edad: int, ubicacion: str, telefono: str, id_credenciales: int) -> None:
        """Método inicializador de un objeto Usuario

        Args:
            id(int)
            nombre(str)
            edad(int)
            telefono(str)
            id_credenciales(int)

        Atributos:
            id(int): Identificador unico
            nombre(str): Nombre real del usuario
            edad(int): Edad del usuario
            telefono(str): Telefono del usuario
            id_credenciales(int): Llave foranea del la clase Credenciales
        """
        super().__init__(id_credenciales)

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.id_credenciales = id_credenciales


    def get_datos(id_credenciales) -> list[tuple]:
        """Método que obtiene los datos principales del usuario por medio de su id de sus credenciales.

        Args:
            id_credenciales(int): Identificador que relaciona la tabla Usuario con sus credenciales.

        Retorno:
            list[tuple]: Los datos extraidos de la base de datos.
        """
        cursor.execute("SELECT NOMBRE, EDAD, UBICACION, TELEFONO FROM USUARIO WHERE ID_CREDENCIALES = :id_c", {'id_c': id_credenciales})
        fila: list[tuple] = cursor.fetchone()
        return fila
    

    def add_usuario(nombre: str, edad: int, ubicacion: str, telefono: str) -> None:
        """Este método añade nuevos nuevas datos y credenciales a nuestra base de datos.

        Args:
            nombre(str): Nombre del nuevo usuario
            edad(int): Edad del nuevo usuario
            ubicacion(str): Ubicacion del nuevo usuario
            telefono(str): Telefono del nuevo usuario

        Retorno: Ninguno
        """
        try:
            cursor.execute("INSERT INTO USUARIO (ID, NOMBRE, EDAD, UBICACION, TELEFONO, ID_CREDENCIALES) VALUES(USUARIO_SEQ.NEXTVAL, :NOMBRE_U, :EDAD_U, :UBICACION_U, :TELEFONO_U, USUARIO_SEQ.CURRVAL)", 
                        {'NOMBRE_U': nombre, 'EDAD_U': edad, 'UBICACION_U': ubicacion, 'TELEFONO_U': telefono})
            
            connection.commit()
        except:

            connection.rollback()
            print("No se pudo crear el nuevo usuario 2")

    def get_amigos(id_usuario: int) -> list[tuple]:
        """Método que retorna todos los amigos de un usuario.

        Args:
            id_usuario(int): Identificador del usuario para obtener los datos

        Retorno:
            list[tuple]: Los amigos del usuario actual
        """
        cursor.execute("SELECT DISTINCT U.NOMBRE, A.FECHA_AMISTAD FROM USUARIO U, USUARIO_AMIGO A WHERE U.ID IN (SELECT ID_AMIGO FROM USUARIO_AMIGO WHERE ID_USUARIO = :ID_U) AND U.ID = A.ID_AMIGO AND A.ID_USUARIO = :ID_U",
                       {'ID_U': id_usuario})
        filas: list[tuple] = cursor.fetchall()

        return filas
    
    def get_nuevas_personas(id_usuario: int) -> tuple:
        """Este método retorna los usuarios que no son amigos del usuario actual.

        Args:
            id_usuario(int): Identificador del usuario para obtener los datos

        Retorno:
            list[tuple]: Posibles personas para agregar como amigo para el usuario actual
        """
        cursor.execute("SELECT C.CORREO FROM USUARIO U, CREDENCIALES C WHERE U.ID NOT IN (SELECT ID_AMIGO FROM USUARIO_AMIGO WHERE ID_USUARIO = :ID_U) AND U.ID_CREDENCIALES = C.ID AND U.ID <> :ID_U",
                       {'ID_U': id_usuario})
        
        filas = cursor.fetchall()
        return filas
    
    def get_id_nuevo_amigo(correo_amigo: str) -> int:
        """Método que obtiene el identificador de el nuevo amigo a agregar

        Args:
            correo_amigo(str): El correo del nuevo amigo para obtener su identificador

        Retorno:
            int: El identificador del nuevo amigo
        """
        cursor.execute("SELECT ID FROM CREDENCIALES WHERE CORREO = :CORREO_AMIGO", {'CORREO_AMIGO': correo_amigo})
        id_usuario_amigo = cursor.fetchone()
        return int(id_usuario_amigo[0])
    
    def add_amigo(id_usuario: int, id_usuario_amigo: int) -> None:
        """Método que añade datos a la tabla USUARIO_AMIGO

        Args:
            id_usuario(int): Identificador del usuario actual
            id_usuario_amigo(int): Identificador del nuevo amigo

        Retorno: Ninguno
        """

        fecha_actual: datetime = datetime.now()
        fecha_amistad_str: str = fecha_actual.strftime('%d/%m/%y')
        print("Actual", id_usuario, "Amigo", id_usuario_amigo, "fecha", fecha_amistad_str)

        cursor_aux = connection.cursor()
       
        try:
        
            cursor_aux.execute("INSERT INTO USUARIO_AMIGO (ID, ID_USUARIO, ID_AMIGO, FECHA_AMISTAD) VALUES (USUARIO_AMIGO_SEQ.NEXTVAL, :ID_USUARIO_U, :ID_AMIGO_U, TO_DATE(:FECHA_AMISTAD, 'DD/MM/YY'))",
                    {'ID_USUARIO_U': id_usuario, 'ID_AMIGO_U': id_usuario_amigo, 'FECHA_AMISTAD': fecha_amistad_str})
                
            connection.commit()
            cursor_aux.execute("INSERT INTO USUARIO_AMIGO (ID, ID_USUARIO, ID_AMIGO, FECHA_AMISTAD) VALUES (USUARIO_AMIGO_SEQ.NEXTVAL, :ID_USUARIO_U, :ID_AMIGO_U, TO_DATE(:FECHA_AMISTAD, 'DD/MM/YY'))",
                    {'ID_USUARIO_U': id_usuario_amigo, 'ID_AMIGO_U': id_usuario, 'FECHA_AMISTAD': fecha_amistad_str})
            
            connection.commit()


            connection.commit()
        except:

            cursor_aux.close()
            connection.rollback()
            print("No se pudo agreagar al amigo", id_usuario, id_usuario_amigo)

        
class Mensaje(Usuario):
    """La clase mensaje representa un mensaje en una aplicacion
    """
    def __init__(self, id: int, contenido: str, fecha_publicacion: datetime, id_usuario_emisor: int, id_usuario_receptor: int) -> None:
        """Método inicializador de un objeto Mensaje

        Args:
            id(int)
            contenido(str)
            fecha_publicacion(str)
            id_usuario_emisor(int)
            id_usuario_receptor(int)

        Atributos:
            id(int): Identificador único
            contenido(str): Contenido del mensaje
            fecha_publicacion(datetime): Fecha de publicación del mensaje
            id_usuario_emisor(int): Identicador del usuario que mandó el mensaje
            id_usuario_receptor(int): Identificador del usuario que recibió el mensaje
        """
        super().__init__(id_usuario_emisor, id_usuario_receptor)

        self.id = id
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion

    def get_mensajes(id_usuario_receptor: int) -> list[tuple]:
        """Método que retorna los mensaje que recibió un usuario

        Args:
            id_usuario_receptor(int): Identificador del usuario receptor

        Retorno:
            list[tuple]: Todos los mensajes que ha recibido el usuario
        """
        cursor.execute("SELECT M.CONTENIDO, U.NOMBRE FROM MENSAJE M, USUARIO U WHERE M.ID_USUARIO_EMISOR = U.ID AND M.ID_USUARIO_RECEPTOR = :ID_R", {'ID_R': id_usuario_receptor})
        filas: list[tuple] = cursor.fetchall()

        return filas
    
    def get_personas(id_usuario_emisor: int) -> list[tuple]:
        """Este método retorna a todos los posibles usuarios al cual el usuario actual puede enviarle un mensaje

        Args:
            id_usuario_emisor(int): Identificador del usuario emisor

        Retorno:
            list[tuple]: La lista de personas al cual se puede enviar un mensaje
        """
        cursor.execute("SELECT CORREO FROM CREDENCIALES WHERE ID <> :ID_E", {'ID_E': id_usuario_emisor})
        filas: list[tuple] = cursor.fetchall()
        return filas
    
    def get_usuario_receptor(correo: str) -> int:
        """Método que retorna el identificador del usuario al cual se le está enviando el mensaje

        Args:
            correo(str): El correo del usuario receptor

        Retorno:
            int: Identificador del usuario receptor
        """
        cursor.execute("SELECT ID FROM CREDENCIALES WHERE CORREO = :CORREO", {'CORREO': correo})
        usuario_receptor = cursor.fetchone()
        return int(usuario_receptor[0])
    
    def add_mensaje(contenido: str, id_usuario_emisor: int, id_usuario_receptor: int) -> None:
        """Método que inserta nuevos datos de un mensaje a la base de datos actual

        Args:
            contenido(str): Contenido del mensaje
            id_usuario_emisor(int): Identificador del usuario emisor del mensaje
            id_usuario_receptor(int): Identificador del usuario receptor del mensaje

        Retorno: Ninguno
        """

        try:
            cursor.execute("INSERT INTO MENSAJE (ID, CONTENIDO, ID_USUARIO_EMISOR, ID_USUARIO_RECEPTOR) VALUES (MENSAJE_SEQ.NEXTVAL, :CONTENIDO_U, :EMISOR_U, :RECEPTOR_U)",
                       {'CONTENIDO_U': contenido, 'EMISOR_U': id_usuario_emisor, 'RECEPTOR_U': id_usuario_receptor})
            
            connection.commit()
        except:

            connection.rollback()
            print("No se pudo enviar el mensaje")
        

def get_noticias() -> list[tuple]:
    """Método que retorna todas las noticias de la base de datos

    Args: None

    Retorno:
        list[tuple]: Todas las noticias publicadas
    """

    cursor.execute("""
                    SELECT N.TITULAR, U.NOMBRE, P.FECHA, P.CONTENIDO, N.FUENTE, L.TEMA_PUBLICACION
                    FROM PUBLICACION P, USUARIO U, NOTICIA N, LISTA_TEMAS L
                    WHERE P.ID_USUARIO = U.ID AND L.ID = P.ID_LISTA_TEMAS AND P.ID = N.ID_PUBLICACION
                    ORDER BY L.TIPO_PUBLICACION ASC
                   """)
    
    filas: list[tuple] = cursor.fetchall()

    return filas

def get_hashtags() -> list[tuple]:
    """Método que retorna todas los hashtags de la base de datos

    Args: None

    Retorno:
        list[tuple]: Todas los hashtags publicados
    """

    cursor.execute("""
                    SELECT U.NOMBRE, P.FECHA, P.CONTENIDO, H.NOMBRE_HASHTAG, L.TEMA_PUBLICACION 
                    FROM PUBLICACION P, USUARIO U, LISTA_TEMAS L, LISTA_HASHTAG H, HASHTAG_PUBLICACION LH
                    WHERE P.ID_USUARIO = U.ID AND L.ID = P.ID_LISTA_TEMAS AND P.ID = LH.ID_PUBLICACION AND LH.ID_HASHTAG = H.ID
                    ORDER BY L.TIPO_PUBLICACION ASC
                   """)
    
    filas: list[tuple] = cursor.fetchall()

    return filas
       
