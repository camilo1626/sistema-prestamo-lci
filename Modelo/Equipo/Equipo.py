from abc import ABC, abstractmethod
from Modelo.Excepciones.EquipoNoDisponibleException import EquipoNoDisponibleException

class Equipo(ABC):
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.prestado = False

    @abstractmethod
    def plazoBase(self):
        pass

    @abstractmethod
    def multaDiaria(self):
        pass

    def requiereAval(self):
        return False

    def calcularPlazo(self, usuario):
        return int(self.plazoBase() * usuario.factorPlazo())

    def verificarPrestable(self):
        if self.prestado:
            raise EquipoNoDisponibleException("EN-01", f"{self.codigo} ya está prestado")
