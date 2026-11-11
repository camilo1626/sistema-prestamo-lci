from datetime import date
from Modelo.Equipo.Portatil import Portatil
from Modelo.Equipo.Microscopio import Microscopio
from Modelo.Equipo.KitArduino import KitArduino
from Modelo.Usuario.Estudiante import Estudiante
from Modelo.Usuario.Docente import Docente
from Modelo.Usuario.Laboratorista import Laboratorista


# Datos iniciales de la sección 6 del taller (vigentes el 2 de marzo de 2026).
# KitArduino: el número es la cantidad de piezas (6 = completo).
# Docente: el último valor es el aval (True = sí tiene aval).
def crearEquipos():
    lista = [
        Portatil("P-01", "Lenovo ThinkPad E14"),
        Portatil("P-02", "Lenovo ThinkPad E14"),
        Portatil("P-03", "HP ProBook 440"),
        Microscopio("M-01", "Microscopio óptico binocular"),
        Microscopio("M-02", "Microscopio óptico binocular"),
        KitArduino("K-01", "Kit Arduino UNO", 6),
        KitArduino("K-02", "Kit Arduino UNO", 5),
        KitArduino("K-03", "Kit Arduino UNO", 6),
    ]
    equipos = {}
    for equipo in lista:
        equipos[equipo.codigo] = equipo
    return equipos


def crearUsuarios():
    lista = [
        Estudiante("E-101", "Camila Rojas", 0),
        Estudiante("E-102", "Andrés Pulido", 0),
        Estudiante("E-103", "Valentina Mora", 14000),
        Docente("D-201", "Roberto Ibáñez", 0, True),
        Docente("D-202", "Marta Pardo", 0, False),
        Laboratorista("L-301", "Jhon Fredy Salcedo", 0),
    ]
    usuarios = {}
    for usuario in lista:
        usuarios[usuario.codigo] = usuario
    return usuarios


# Las 25 peticiones de la sección 8, en orden.
# Cada una: (accion, usuario, equipo, fecha, simular falla de guardado)
def crearPeticiones():
    d2 = date(2026, 3, 2)
    d3 = date(2026, 3, 3)
    d6 = date(2026, 3, 6)
    d7 = date(2026, 3, 7)
    d9 = date(2026, 3, 9)
    return [
        ("prestar", "E-101", "P-01", d2, False),
        ("prestar", "E-101", "M-01", d2, False),
        ("prestar", "D-201", "M-01", d2, False),
        ("prestar", "D-202", "M-02", d2, False),
        ("prestar", "E-103", "P-02", d2, False),
        ("prestar", "E-102", "K-02", d2, False),
        ("reservar", "E-102", "K-02", d2, False),
        ("reservar", "E-103", "K-02", d2, False),
        ("prestar", "E-102", "P-01", d2, False),
        ("prestar", "E-102", "P-02", d2, False),
        ("prestar", "E-102", "P-03", d2, False),
        ("prestar", "E-102", "K-01", d2, False),
        ("prestar", "L-301", "M-02", d2, False),
        ("reservar", "E-101", "M-02", d2, False),
        ("prestar", "D-202", "K-01", d2, False),
        ("prestar", "E-101", "K-03", d3, True),
        ("prestar", "E-101", "K-03", d3, False),
        ("devolver", "-", "M-02", d6, False),
        ("devolver", "-", "P-01", d7, False),
        ("devolver", "-", "P-02", d7, False),
        ("devolver", "-", "P-03", d9, False),
        ("devolver", "-", "M-01", d9, False),
        ("devolver", "-", "K-01", d9, False),
        ("prestar", "E-102", "P-01", d9, False),
        ("prestar", "D-201", "K-02", d9, False),
    ]
