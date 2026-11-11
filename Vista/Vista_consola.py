from datetime import datetime

class VistaConsola:
    def menu(self):
        print("\n=== Sistema de préstamos del LCI ===")
        print("1. Prestar")
        print("2. Devolver")
        print("3. Reservar")
        print("4. Ver multas")
        print("5. Ver log")
        print("6. Correr peticiones del mostrador")
        print("0. Salir")
        return input("Opción: ").strip()

    def pedirCodigo(self, etiqueta):
        return input(f"Código de {etiqueta}: ").strip().upper()

    def pedirFecha(self):
        return self.convertirFecha(input("Fecha (dd/mm/aaaa): "))
    
    def convertirFecha(self, texto):
        return datetime.strptime(texto.strip(), "%d/%m/%Y").date()

    def mostrar(self, mensaje):
        print(mensaje)

    def mostrarMultas(self, filas):
        for codigo, nombre, multas in filas:
            multaTexto = f"{multas:,}".replace(",", ".")
            print(f"{codigo} {nombre}: ${multaTexto}")

    def mostrarLog(self, lineas):
        if not lineas:
            print("El log está vacío.")
        for linea in lineas:
            print(linea)
