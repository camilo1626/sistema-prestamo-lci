from Modelo.Equipo.Equipo import Equipo

class Microscopio(Equipo):
    def plazoBase(self):
        return 2

    def multaDiaria(self):
        return 10000

    def requiereAval(self):
        return True
