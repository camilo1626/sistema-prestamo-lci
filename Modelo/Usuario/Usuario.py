from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, codigo, nombre, multas=0):
        self.codigo = codigo
        self.nombre = nombre
        self.multas = multas  # deuda pendiente en pesos

    def tieneMultaPendiente(self):
        return self.multas > 0

    def tieneAval(self):
        return False

    @abstractmethod
    def cupoMaximo(self):
        pass

    @abstractmethod
    def factorPlazo(self):
        pass
