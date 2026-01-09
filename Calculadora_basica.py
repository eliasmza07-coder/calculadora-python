class Calculadora:
    """Calculadora básica con operaciones aritméticas."""

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b


class Interfaz:
    """Maneja la interacción con el usuario."""

    OPCIONES = {
        1: ("Suma", "sumar"),
        2: ("Resta", "restar"),
        3: ("Multiplicación", "multiplicar"),
        4: ("División", "dividir"),
        0: ("Salir", None)
    }

    @staticmethod
    def mostrar_menu():
        print("\n--- Calculadora Básica ---")
        for clave, (nombre, _) in Interfaz.OPCIONES.items():
            print(f"{clave}: {nombre}")
        print("-------------------------")

    @staticmethod
    def pedir_numero(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: Ingrese un número válido.")

    @staticmethod
    def pedir_opcion():
        while True:
            try:
                opcion = int(input("Seleccione una opción:\n> "))
                if opcion in Interfaz.OPCIONES:
                    return opcion
                print("Opción inválida.")
            except ValueError:
                print("Ingrese un número de opción.")


def main():
    calculadora = Calculadora()

    while True:
        Interfaz.mostrar_menu()
        opcion = Interfaz.pedir_opcion()

        if opcion == 0:
            print("Gracias por usar la calculadora")
            break

        n1 = Interfaz.pedir_numero("Ingrese el primer número:\n> ")
        n2 = Interfaz.pedir_numero("Ingrese el segundo número:\n> ")

        _, metodo = Interfaz.OPCIONES[opcion]

        try:
            operacion = getattr(calculadora, metodo)
            resultado = operacion(n1, n2)
            print(f"Resultado: {resultado}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()



