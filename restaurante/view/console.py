from restaurante.model.restaurante import Restaurante, Nomina


class ConsolaRestaurante:
    def __init__(self):
        self.restaurante = Restaurante()

    def mostrar_menu(self):
        print("=== Restaurante ===")
        print("1. Agregar mesero")
        print("2. Generar horarios")
        print("3. Calcular nómina")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.registrar_mesero()
            elif opcion == "2":
                self.generar_horarios()
            elif opcion == "3":
                self.calcular_nomina()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def registrar_mesero(self):
        nombre = input("Ingrese el nombre del mesero: ")
        correo = input("Ingrese el correo del mesero: ")
        self.restaurante.agregar_mesero(nombre, correo)
        print("Mesero registrado exitosamente.")

    def generar_horarios(self):

        if len(self.restaurante.meseros) > 8:
            horarios = self.restaurante.generar_horarios()
            for dia, turnos in horarios.items():
                print(f"{dia}:")
                for turno in turnos:
                    print(turno)
        else:
            raise ValueError("No hay suficientes meseros para cubrir los turnos en semana.")
    def calcular_nomina(self):
        nomina = Nomina(self.restaurante.meseros)
        salarios = nomina.calcular_salario()
        for mesero, salario in salarios.items():
            print(f"{mesero}: ${salario}")


# Ejemplo de uso de la consola
consola = ConsolaRestaurante()
consola.ejecutar()