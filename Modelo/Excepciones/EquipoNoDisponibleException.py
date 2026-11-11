from Modelo.Excepciones.PrestamoException import PrestamoException


# Se lanza cuando el equipo no se puede prestar.
# EN-01: el equipo ya está prestado.
# EN-02: el kit está incompleto.
class EquipoNoDisponibleException(PrestamoException):
    def __init__(self, codigo, mensajeTecnico):
        if codigo == "EN-02":
            mensaje = "Este kit está incompleto. Se puede reservar, pero no prestar por ahora."
        else:
            mensaje = "Este equipo ya está prestado en este momento."
        super().__init__(codigo, mensaje, mensajeTecnico)
