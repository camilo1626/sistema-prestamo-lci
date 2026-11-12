# Pruebas del sistema. Ejecutar desde la carpeta TALLER1:  python pruebas.py
import os
from datetime import date
from Controlador.PrestamoController import PrestamoController
from Controlador.Datos import crearPeticiones
from Vista.Vista_consola import VistaConsola

# Texto que debe aparecer en el resultado de cada una de las 25 peticiones.
ESPERADOS = [
    "Devuelva Lenovo ThinkPad E14 antes del 07/03/2026.",       # 1  E-101 P-01
    "Este equipo solo se presta con aval del departamento.",     # 2  E-101 M-01
    "Devuelva Microscopio óptico binocular antes del 05/03/2026.",  # 3  D-201 M-01
    "Este equipo solo se presta con aval del departamento.",     # 4  D-202 M-02
    "Tiene una multa pendiente",                                 # 5  E-103 P-02
    "Este kit está incompleto",                                  # 6  E-102 K-02
    "Reserva registrada para Kit Arduino UNO.",                  # 7  reserva K-02
    "Tiene una multa pendiente",                                 # 8  E-103 reserva K-02
    "Este equipo ya está prestado",                              # 9  E-102 P-01
    "Devuelva Lenovo ThinkPad E14 antes del 07/03/2026.",       # 10 E-102 P-02
    "Devuelva HP ProBook 440 antes del 07/03/2026.",             # 11 E-102 P-03
    "Ya alcanzó el número máximo",                               # 12 E-102 K-01
    "Devuelva Microscopio óptico binocular antes del 06/03/2026.",  # 13 L-301 M-02
    "Reserva registrada para Microscopio",                       # 14 E-101 reserva M-02
    "Devuelva Kit Arduino UNO antes del 12/03/2026.",           # 15 D-202 K-01
    "No fue posible completar la operación",                     # 16 falla simulada
    "Devuelva Kit Arduino UNO antes del 10/03/2026.",           # 17 reintento K-03
    "Equipo devuelto a tiempo.",                                 # 18 M-02
    "Equipo devuelto a tiempo.",                                 # 19 P-01
    "Equipo devuelto a tiempo.",                                 # 20 P-02
    "Equipo devuelto con 2 día(s) de retraso. Multa: $4.000.",  # 21 P-03
    "Equipo devuelto con 4 día(s) de retraso. Multa: $40.000.", # 22 M-01
    "Equipo devuelto a tiempo.",                                 # 23 K-01
    "Tiene una multa pendiente",                                 # 24 E-102 P-01
    "Tiene una multa pendiente",                                 # 25 D-201 K-02
]

fallos = 0


def comprobar(nombre, condicion):
    global fallos
    if condicion:
        print(f"  OK     {nombre}")
    else:
        print(f"  FALLO  {nombre}")
        fallos += 1


def prueba_25_peticiones():
    print("\n[1] Las 25 peticiones del mostrador")
    controlador = PrestamoController()
    resultados = []
    for accion, usuario, equipo, fecha, falla in crearPeticiones():
        resultados.append(controlador.procesarPeticion(accion, usuario, equipo, fecha, falla))

    for numero, (resultado, esperado) in enumerate(zip(resultados, ESPERADOS), 1):
        comprobar(f"petición {numero:2}: {esperado}", esperado in resultado)

    print("\n[2] Estado final")
    comprobar("multa de E-102 Andrés = 4000", controlador.usuarios["E-102"].multas == 4000)
    comprobar("multa de D-201 Roberto = 40000", controlador.usuarios["D-201"].multas == 40000)
    comprobar("multa de E-103 Valentina = 14000 (sin cambio)", controlador.usuarios["E-103"].multas == 14000)
    comprobar("multa de E-101 Camila = 0", controlador.usuarios["E-101"].multas == 0)
    comprobar("K-03 sigue prestado a Camila", controlador.equipos["K-03"].prestado is True)
    libres = [c for c, e in controlador.equipos.items() if c != "K-03" and e.prestado]
    comprobar("ningún otro equipo queda prestado", libres == [])
    comprobar("K-02 quedó reservado (no prestado)", controlador.equipos["K-02"].prestado is False)
    comprobar("log con exactamente un SYS-00 (petición 16)",
              sum(1 for linea in controlador.verLog() if "SYS-00" in linea) == 1)
    comprobar("log con 9 errores de negocio (peticiones 2,4,5,6,8,9,12,24,25)",
              sum(1 for linea in controlador.verLog() if "SYS-00" not in linea) == 9)


def prueba_rollback():
    print("\n[3] Rollback: el guardado falla")
    controlador = PrestamoController()
    antes_prestado = controlador.equipos["K-03"].prestado
    antes_prestamos = len(controlador.prestamos)
    mensaje = controlador.procesarPeticion("prestar", "E-101", "K-03", date(2026, 3, 3), True)
    comprobar("el usuario ve el mensaje genérico", mensaje == "No fue posible completar la operación. Intente de nuevo.")
    comprobar("K-03 vuelve a estar como antes (prestado = False)",
              controlador.equipos["K-03"].prestado == antes_prestado)
    comprobar("no se guardó ningún préstamo", len(controlador.prestamos) == antes_prestamos)
    comprobar("la bandera de simulación se apaga después",
              controlador.simularFallaGuardado is False)


def prueba_codigos_invalidos():
    print("\n[4] Códigos inválidos (nunca deben mostrar un error técnico)")
    controlador = PrestamoController()
    d = date(2026, 3, 2)
    casos = [
        ("usuario inexistente al prestar", controlador.prestar("E-999", "P-01", d)),
        ("equipo inexistente al prestar", controlador.prestar("E-101", "P-99", d)),
        ("usuario inexistente al reservar", controlador.reservar("X-1", "P-01", d)),
        ("equipo inexistente al reservar", controlador.reservar("E-101", "Z-9", d)),
        ("equipo inexistente al devolver", controlador.devolver("Z-9", d)),
    ]
    for nombre, mensaje in casos:
        comprobar(f"{nombre}: mensaje sin texto técnico",
                  "KeyError" not in mensaje and "No existe" not in mensaje and mensaje != "")
    comprobar("los códigos inválidos quedan en el log",
              sum(1 for linea in controlador.verLog() if "SYS-00" in linea) == 5)


def prueba_devolver_sin_prestamo():
    print("\n[5] Devolver un equipo que no está prestado")
    controlador = PrestamoController()
    comprobar("respuesta clara",
              controlador.devolver("P-01", date(2026, 3, 2)) == "Este equipo no está prestado.")


def prueba_fechas():
    print("\n[6] Fechas incorrectas (la vista)")
    vista = VistaConsola()
    comprobar("02/03/2026 es válida", vista.convertirFecha("02/03/2026") == date(2026, 3, 2))
    for malo in ["31/02/2026", "2026-03-02", "hoy", "02-03-2026", ""]:
        try:
            vista.convertirFecha(malo)
            comprobar(f"'{malo}' debe rechazarse", False)
        except ValueError:
            comprobar(f"'{malo}' se rechaza", True)


def prueba_polimorfismo():
    print("\n[7] Polimorfismo (valores de cada clase)")
    from Modelo.Equipo.Portatil import Portatil
    from Modelo.Equipo.Microscopio import Microscopio
    from Modelo.Equipo.KitArduino import KitArduino
    from Modelo.Usuario.Estudiante import Estudiante
    from Modelo.Usuario.Docente import Docente
    from Modelo.Usuario.Laboratorista import Laboratorista
    est = Estudiante("E-X", "x")
    doc = Docente("D-X", "y")
    lab = Laboratorista("L-X", "z")
    comprobar("portátil: plazo 5 / 7 / 10", (Portatil("P", "p").calcularPlazo(est),
              Portatil("P", "p").calcularPlazo(doc), Portatil("P", "p").calcularPlazo(lab)) == (5, 7, 10))
    comprobar("microscopio: plazo 2 / 3 / 4", (Microscopio("M", "m").calcularPlazo(est),
              Microscopio("M", "m").calcularPlazo(doc), Microscopio("M", "m").calcularPlazo(lab)) == (2, 3, 4))
    comprobar("cupo 2 / 4 / 6", (est.cupoMaximo(), doc.cupoMaximo(), lab.cupoMaximo()) == (2, 4, 6))
    comprobar("multa diaria 2000 / 10000 / 1500",
              (Portatil("P", "p").multaDiaria(), Microscopio("M", "m").multaDiaria(),
               KitArduino("K", "k", 6).multaDiaria()) == (2000, 10000, 1500))


def prueba_excepciones():
    print("\n[8] Excepciones: código y mensajes")
    from Modelo.Excepciones.PrestamoException import PrestamoException
    from Modelo.Excepciones.UsuarioBloqueadoException import UsuarioBloqueadoException
    from Modelo.Excepciones.EquipoNoDisponibleException import EquipoNoDisponibleException
    from Modelo.Excepciones.AvalRequeridoException import AvalRequeridoException
    from Modelo.Excepciones.CupoExcedidoException import CupoExcedidoException
    ub = UsuarioBloqueadoException("tecnico")
    comprobar("UB-01 hereda de PrestamoException", issubclass(UsuarioBloqueadoException, PrestamoException) and ub.codigo == "UB-01")
    comprobar("EN-01 y EN-02 con mensajes distintos",
              EquipoNoDisponibleException("EN-01", "t").mensajeUsuario != EquipoNoDisponibleException("EN-02", "t").mensajeUsuario)
    comprobar("AV-01", AvalRequeridoException("t").codigo == "AV-01")
    comprobar("CE-01", CupoExcedidoException("t").codigo == "CE-01")
    comprobar("el mensaje técnico se guarda aparte", ub.mensajeTecnico == "tecnico")


if __name__ == "__main__":
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    prueba_25_peticiones()
    prueba_rollback()
    prueba_codigos_invalidos()
    prueba_devolver_sin_prestamo()
    prueba_fechas()
    prueba_polimorfismo()
    prueba_excepciones()
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    print("\n" + ("TODAS LAS PRUEBAS PASARON" if fallos == 0 else f"HAY {fallos} PRUEBA(S) CON FALLO"))
    raise SystemExit(1 if fallos else 0)
