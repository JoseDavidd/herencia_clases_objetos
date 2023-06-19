from generarNombre import GenerarNombre

class User:
    def __init__(self):
        gen = GenerarNombre()
        self.nombre = gen.get_nombre()
        self.correo = gen.get_correo()

        def __str__(self):
            return f"{self.nombre} - {self.correo}"
