# Clase base de todos los errores del préstamo.
# Cada error tiene tres cosas:
#   codigo          -> código del error (UB-01, EN-01, EN-02, AV-01, CE-01, SYS-00)
#   mensajeUsuario  -> mensaje respetuoso que sí puede ver el estudiante
#   mensajeTecnico  -> detalle técnico que solo se guarda en el log


class PrestamoException(Exception):
    def __init__(self, codigo, mensajeUsuario, mensajeTecnico):
        super().__init__(mensajeTecnico)
        self.codigo = codigo
        self.mensajeUsuario = mensajeUsuario
        self.mensajeTecnico = mensajeTecnico
