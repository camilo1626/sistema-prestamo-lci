from Modelo.Usuario.Usuario import Usuario

class Laboratorista(Usuario):
    def cupoMaximo(self):
        return 6

    def factorPlazo(self):
        return 2

    def tieneAval(self):
        return True
