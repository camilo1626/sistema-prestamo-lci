from Modelo.Excepciones.PrestamoException import PrestamoException


# Se lanza cuando la persona tiene multa pendiente (préstamo o reserva).
class UsuarioBloqueadoException(PrestamoException):
    def __init__(self, mensajeTecnico):
        super().__init__(
            "UB-01",
            "Tiene una multa pendiente. Debe pagarla en caja para pedir o reservar equipos.",
            mensajeTecnico,
        )
