from Modelo.Usuario.Usuario import Usuario


class Estudiante(Usuario):
    def cupoMaximo(self):
        return 2

    def factorPlazo(self):
        return 1
