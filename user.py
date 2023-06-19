from generarNombre import GenerarNombre

class User:

    def __init__(self, nombre, correo):
        gen = GenerarNombre()
        self.nombre = gen.get_nombre()
        self.correo = gen.get_correo()
        

  
