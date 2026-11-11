from Modelo.Excepciones.PrestamoException import PrestamoException


# Se lanza cuando la persona ya tiene el máximo de equipos prestados.
class CupoExcedidoException(PrestamoException):
    def __init__(self, mensajeTecnico):
        super().__init__(
            "CE-01",
            "Ya alcanzó el número máximo de equipos permitidos.",
            mensajeTecnico,
        )
