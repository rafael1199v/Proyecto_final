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

class Usuario(Credenciales):
    def __init__(self, id: int, nombre_usuario: str, correo: str, contrasenha: str, nombre: str, edad: int, ubicacion: str, telefono: str, id_credenciales: int) -> None:
        super().__init__(id, nombre_usuario, correo, contrasenha)

        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.id_credenciales = id_credenciales


    def agregar_amigo(self, other) -> None:
        pass

class Administrador(Credenciales):
    def __init__(self, id: int, nombre_usuario: str, correo: str, contrasenha: str, nombre: str, edad: int, ubicacion: str, telefono: str, id_credenciales: int) -> None:
        super().__init__(id, nombre_usuario, correo, contrasenha)

        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.id_credenciales = id_credenciales


class TipoPublicacion():
    def __init__(self, id: int, tema_publicacion: str, tipo_publicacion: str) -> None:
        self.id = id
        self.tema_publicacion = tema_publicacion
        self.tipo_publicacion = tipo_publicacion

class Noticia(Usuario, TipoPublicacion):
    def __init__(self, id: int, contenido: str, fecha: str, titular: str, fuente: str, id_usuario: int, id_tipo: int) -> None:
        super.__init__(id_usuario, id_tipo)
        self.id = id
        self.contenido = contenido
        self.fecha = fecha
        self.titular = titular
        self.fuente = fuente


    def get_noticia(self) -> str:
        return (f"{self.titular}\n"
                f"{self.contenido}\n")
    

    def get_fecha(self) -> str:
        return self.fecha
    



class Mensaje(Usuario):

    def __init__(self, id: int, contenido: str, fecha_publicacion: str, id_usuario_emisor: int, id_usuario_receptor: int) -> None:
        super().__init__(id_usuario_emisor, id_usuario_receptor)

        self.id = id
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
    
    pass

class Publicacion():
    def __init__(self, id: int, tamanho_publicacion: str, contenido: str, fecha: str, restriccion_solo_amigos: bool, id_usuario: int, id_tipo: int) -> None:
        super.__init__(id_usuario, id_tipo)
        self.id = id
        self.tamanho_publicacion = tamanho_publicacion
        self.contenido = contenido
        self.fecha = fecha
        self.restriccion_solo_amigos = restriccion_solo_amigos

    def get_publicacion(self) -> str:
        return (f"{self.contenido}\n")
    

    def get_fecha(self) -> str:
        return self.fecha
