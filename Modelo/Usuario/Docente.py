from Modelo.Usuario.Usuario import Usuario


class Docente(Usuario):
    def __init__(self, codigo, nombre, multas=0, aval=False):
        super().__init__(codigo, nombre, multas)
        self.aval = aval

    def cupoMaximo(self):
        return 4

    def factorPlazo(self):
        return 1.5

    def tieneAval(self):
        return self.aval
