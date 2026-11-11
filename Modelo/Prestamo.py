from datetime import timedelta


# Un préstamo guarda quién tiene qué, desde cuándo y hasta cuándo.
class Prestamo:
    def __init__(self, usuario, equipo, fecha, plazo):
        self.usuario = usuario
        self.equipo = equipo
        self.fechaPrestamo = fecha
        self.fechaLimite = fecha + timedelta(days=plazo)
        self.fechaDevolucion = None  # se llena cuando se devuelve

    def estaActivo(self):
        return self.fechaDevolucion is None

    # Días de retraso después de la fecha límite (0 si devolvió a tiempo).
    def calcularRetraso(self, fechaDevolucion):
        dias = (fechaDevolucion - self.fechaLimite).days
        if dias < 0:
            return 0
        return dias

    # Multa = días de retraso x multa diaria del equipo.
    def calcularMulta(self, fechaDevolucion):
        return self.calcularRetraso(fechaDevolucion) * self.equipo.multaDiaria()
