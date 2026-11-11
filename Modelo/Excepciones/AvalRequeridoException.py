from Modelo.Excepciones.PrestamoException import PrestamoException


# Se lanza cuando el equipo exige aval (microscopio) y la persona no lo tiene.
class AvalRequeridoException(PrestamoException):
    def __init__(self, mensajeTecnico):
        super().__init__(
            "AV-01",
            "Este equipo solo se presta con aval del departamento.",
            mensajeTecnico,
        )
