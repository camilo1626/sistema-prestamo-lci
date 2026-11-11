from datetime import datetime
from Controlador.Datos import crearEquipos, crearUsuarios
from Modelo.Prestamo import Prestamo
from Modelo.Excepciones.PrestamoException import PrestamoException
from Modelo.Excepciones.UsuarioBloqueadoException import UsuarioBloqueadoException
from Modelo.Excepciones.AvalRequeridoException import AvalRequeridoException
from Modelo.Excepciones.CupoExcedidoException import CupoExcedidoException

# Lo único que la vista puede mostrar cuando falla algo inesperado.
MENSAJE_SYS = "No fue posible completar la operación. Intente de nuevo."
ARCHIVO_LOG = "log.txt"



class PrestamoController:
    def __init__(self):
        self.equipos = crearEquipos()
        self.usuarios = crearUsuarios()
        self.prestamos = []
        self.reservas = []
        self.log = []
        # Para pruebas: si está en True, el siguiente guardado falla.
        self.simularFallaGuardado = False


    def _buscarUsuario(self, codigo):
        if codigo not in self.usuarios:
            raise KeyError(f"No existe el usuario {codigo}")
        return self.usuarios[codigo]

    def _buscarEquipo(self, codigo):
        if codigo not in self.equipos:
            raise KeyError(f"No existe el equipo {codigo}")
        return self.equipos[codigo]

    def _cupoUsado(self, usuario):
        contador = 0
        for prestamo in self.prestamos:
            if prestamo.usuario.codigo == usuario.codigo and prestamo.estaActivo():
                contador += 1
        return contador

    def _guardar(self, prestamo):
        if self.simularFallaGuardado:
            raise IOError("Se perdió la conexión con el servidor de archivos")
        self.prestamos.append(prestamo)

    def _registrar(self, codigo, mensajeTecnico):
        linea = f"{datetime.now():%Y-%m-%d %H:%M:%S} | {codigo} | {mensajeTecnico}"
        self.log.append(linea)
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(linea + "\n")

    def _responderError(self, error):
        self._registrar(error.codigo, error.mensajeTecnico)
        return error.mensajeUsuario

    def _responderFallaInesperada(self, error):
        self._registrar("SYS-00", f"{type(error).__name__}: {error}")
        return MENSAJE_SYS

    def prestar(self, codigoUsuario, codigoEquipo, fecha):
        try:
            usuario = self._buscarUsuario(codigoUsuario)
            equipo = self._buscarEquipo(codigoEquipo)

            if usuario.tieneMultaPendiente():
                raise UsuarioBloqueadoException(f"{usuario.codigo} tiene multa de {usuario.multas}")
            
            equipo.verificarPrestable()

            if equipo.requiereAval() and not usuario.tieneAval():
                raise AvalRequeridoException(
                    f"{usuario.codigo} no tiene aval para {equipo.codigo}"
                )

            if self._cupoUsado(usuario) >= usuario.cupoMaximo():
                raise CupoExcedidoException(
                    f"{usuario.codigo} ya tiene {usuario.cupoMaximo()} equipos"
                )

            prestamo = Prestamo(usuario, equipo, fecha, equipo.calcularPlazo(usuario))

            anterior = equipo.prestado
            equipo.prestado = True
            try:
                self._guardar(prestamo)
            except Exception:
                equipo.prestado = anterior
                raise

            return (f"Préstamo registrado. Devuelva {equipo.descripcion} "f"antes del {prestamo.fechaLimite:%d/%m/%Y}.")

        except PrestamoException as error:
            return self._responderError(error)
        except Exception as error:
            return self._responderFallaInesperada(error)

    def reservar(self, codigoUsuario, codigoEquipo, fecha):
        try:
            usuario = self._buscarUsuario(codigoUsuario)
            equipo = self._buscarEquipo(codigoEquipo)

            if usuario.tieneMultaPendiente():
                raise UsuarioBloqueadoException(
                    f"{usuario.codigo} tiene multa de {usuario.multas}"
                )

            self.reservas.append(
                {"usuario": usuario.codigo, "equipo": equipo.codigo, "fecha": fecha}
            )
            return f"Reserva registrada para {equipo.descripcion}."

        except PrestamoException as error:
            return self._responderError(error)
        except Exception as error:
            return self._responderFallaInesperada(error)

    def devolver(self, codigoEquipo, fecha):
        try:
            equipo = self._buscarEquipo(codigoEquipo)

            prestamoActivo = None
            for prestamo in self.prestamos:
                if prestamo.equipo.codigo == codigoEquipo and prestamo.estaActivo():
                    prestamoActivo = prestamo
                    break

            if prestamoActivo is None:
                return "Este equipo no está prestado."

            dias = prestamoActivo.calcularRetraso(fecha)
            multa = prestamoActivo.calcularMulta(fecha)

            prestamoActivo.fechaDevolucion = fecha
            equipo.prestado = False
            prestamoActivo.usuario.multas += multa

            if multa == 0:
                return "Equipo devuelto a tiempo. Gracias."

            multaTexto = f"{multa:,}".replace(",", ".")
            return (
                f"Equipo devuelto con {dias} día(s) de retraso. "
                f"Multa: ${multaTexto}. Debe pagarla en caja."
            )

        except Exception as error:
            return self._responderFallaInesperada(error)

    def procesarPeticion(self, accion, codigoUsuario, codigoEquipo, fecha, simularFalla):
        self.simularFallaGuardado = simularFalla
        try:
            if accion == "prestar":
                return self.prestar(codigoUsuario, codigoEquipo, fecha)
            if accion == "reservar":
                return self.reservar(codigoUsuario, codigoEquipo, fecha)
            return self.devolver(codigoEquipo, fecha)
        finally:
            self.simularFallaGuardado = False

    def multasPorPersona(self):
        filas = []
        for usuario in self.usuarios.values():
            filas.append((usuario.codigo, usuario.nombre, usuario.multas))
        return filas

    def verLog(self):
        return self.log
