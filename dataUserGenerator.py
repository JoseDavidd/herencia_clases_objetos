from generarNombre import GenerarNombre

class dataUserGenerator:
    def __init__(self):
        gen = GenerarNombre()
        self.nombre = gen.get_nombre()
        self.turno = "A"
        self.correo = gen.get_correo()

        def __str__(self):
            return f"{self.nombre} - {self.turno} - {self.correo}"
        result =  __str__(self)
        print(result) 