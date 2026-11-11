from Modelo.Equipo.Equipo import Equipo
from Modelo.Excepciones.EquipoNoDisponibleException import EquipoNoDisponibleException

PIEZAS_COMPLETO = 6


# Kit Arduino: plazo base 7 días, multa diaria $1.500.
class KitArduino(Equipo):
    def __init__(self, codigo, descripcion, piezas):
        super().__init__(codigo, descripcion)
        self.piezas = piezas

    def plazoBase(self):
        return 7

    def multaDiaria(self):
        return 1500

    def verificarPrestable(self):
        super().verificarPrestable()
        
        
        if self.piezas < PIEZAS_COMPLETO:
            raise EquipoNoDisponibleException("EN-02", f"{self.codigo} tiene {self.piezas} de {PIEZAS_COMPLETO} piezas")