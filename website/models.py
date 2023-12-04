from .data import cursor

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
        cursor.execute("SELECT * FROM credenciales WHERE correo = :correo", {'correo': correo})
        fila = cursor.fetchone()
        return fila
        


class Usuario(Credenciales):
    def __init__(self, id, nombre: str, edad: int, ubicacion: str, telefono: str, id_credenciales: int) -> None:
        super().__init__(id_credenciales)

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.id_credenciales = id_credenciales

    def agregar_amigo(self, other) -> None:
        pass


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
    
