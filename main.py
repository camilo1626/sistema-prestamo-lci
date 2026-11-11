from Controlador.PrestamoController import PrestamoController
from Controlador.Datos import crearPeticiones
from Vista.Vista_consola import VistaConsola


def correrPeticiones(controlador, vista):
    numero = 0
    for accion, usuario, equipo, fecha, falla in crearPeticiones():
        numero += 1
        resultado = controlador.procesarPeticion(accion, usuario, equipo, fecha, falla)
        if accion == "devolver":
            texto = f"devuelve {equipo}"
        elif accion == "reservar":
            texto = f"{usuario} reserva {equipo}"
        else:
            texto = f"{usuario} pide {equipo}"
        vista.mostrar(f"{numero:2}. {fecha:%d/%m} {texto}")
        vista.mostrar(f"    -> {resultado}")


def main():
    controlador = PrestamoController()
    vista = VistaConsola()

    while True:
        opcion = vista.menu()

        try:
            if opcion == "1":
                usuario = vista.pedirCodigo("usuario")
                equipo = vista.pedirCodigo("equipo")
                fecha = vista.pedirFecha()
                vista.mostrar(controlador.prestar(usuario, equipo, fecha))

            elif opcion == "2":
                equipo = vista.pedirCodigo("equipo")
                fecha = vista.pedirFecha()
                vista.mostrar(controlador.devolver(equipo, fecha))

            elif opcion == "3":
                usuario = vista.pedirCodigo("usuario")
                equipo = vista.pedirCodigo("equipo")
                fecha = vista.pedirFecha()
                vista.mostrar(controlador.reservar(usuario, equipo, fecha))

            elif opcion == "4":
                vista.mostrarMultas(controlador.multasPorPersona())

            elif opcion == "5":
                vista.mostrarLog(controlador.verLog())

            elif opcion == "6":
                correrPeticiones(controlador, vista)
                print("\n--- Multas al final ---")
                vista.mostrarMultas(controlador.multasPorPersona())
                print("\n--- Log ---")
                vista.mostrarLog(controlador.verLog())

            elif opcion == "0":
                break

            else:
                vista.mostrar("Opción no válida.")

        except ValueError:
            vista.mostrar("La fecha no es válida. Use el formato dd/mm/aaaa.")


if __name__ == "__main__":
    main()
