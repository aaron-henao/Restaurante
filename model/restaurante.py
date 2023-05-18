import random

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

class Mesero:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.dias_descanso = 0
        self.horas_trabajadas = 0


class Restaurante:
    def __init__(self):
        self.meseros = []
        self.horas_trabajadas = 0

    def agregar_mesero(self, nombre: str, correo: str):
        mesero = Mesero(nombre, correo)
        self.meseros.append(mesero)

    def generar_horarios(self):
        turnos = [
            "11:00 am - 18:00 pm",
            "11:00 am - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - 15:00 pm - 18:00 pm - cierre",
            "12:00 pm - cierre"
        ]
        horarios = {dia: [] for dia in dias_semana}
        meseros_disponibles = self.meseros.copy()

        for dia in dias_semana:
            if dia in ["Lunes", "Martes", "Miércoles"]:
                max_meseros_descanso = 3  # Hasta tres meseros pueden descansar estos días
            else:
                max_meseros_descanso = 2  # Dos meseros pueden descansar los demás días

            meseros_descanso = []
            meseros_cierre = []  # Meseros asignados al turno "12:00 pm - cierre"
            turno = random.choice(turnos)
            for mesero in meseros_disponibles:
                if mesero.dias_descanso < 2 and len(meseros_descanso) < max_meseros_descanso:
                    meseros_descanso.append(mesero)
                    mesero.dias_descanso += 1
                elif len(meseros_cierre) < 2 and turno == "12:00 pm - cierre":
                    meseros_cierre.append(mesero)

            for mesero in meseros_disponibles:
                if mesero in meseros_descanso:
                    horarios[dia].append(mesero.nombre + ": Descanso")
                elif mesero in meseros_cierre:
                    horarios[dia].append(mesero.nombre + ": 12:00 pm - cierre")
                else:
                    turno = random.choice(turnos)
                    horas_turno = 0
                    if turno == "11:00 am - 18:00 pm":
                        horas_turno = 7
                    elif turno == "11:00 am - 15:00 pm - 18:00 pm - cierre":
                        horas_turno = 9
                    elif turno == "12:00 pm - 15:00 pm - 18:00 pm - cierre":
                        horas_turno = 8
                    else:
                        horas_turno = 10

                    if mesero.horas_trabajadas + horas_turno <= 48:
                        horarios[dia].append(mesero.nombre + " : " + turno)
                        mesero.horas_trabajadas += horas_turno
                        self.horas_trabajadas += horas_turno
                    else:
                        horarios[dia].append(mesero.nombre + ": Descanso (Exceso de horas)")

            meseros_disponibles = self.meseros.copy()

        return horarios


class Nomina:
    def __init__(self, meseros):
        self.meseros = meseros

    def calcular_salario(self):
        valor_hora = 4830
        salarios = {}
        for mesero in self.meseros:
            salario = mesero.horas_trabajadas * valor_hora
            salarios[mesero.nombre] = salario
        return salarios


restaurante = Restaurante()

restaurante.agregar_mesero("Mesero 1", "mesero1@example.com")
restaurante.agregar_mesero("Mesero 2", "mesero2@example.com")
restaurante.agregar_mesero("Mesero 3", "mesero3@example.com")
restaurante.agregar_mesero("Mesero 4", "mesero4@example.com")
restaurante.agregar_mesero("Mesero 5", "mesero5@example.com")
restaurante.agregar_mesero("Mesero 6", "mesero6@example.com")
restaurante.agregar_mesero("Mesero 7", "mesero7@example.com")
restaurante.agregar_mesero("Mesero 8", "mesero8@example.com")
restaurante.agregar_mesero("Mesero 9", "mesero9@example.com")

horarios_semana = restaurante.generar_horarios()

for dia, horarios in horarios_semana.items():
    print(dia)
    for horario in horarios:
        print(horario)
    print()

# Mostrar horas laboradas por cada mesero por día y total a la semana
for mesero in restaurante.meseros:
    print(f"{mesero.nombre} - Horas diarias: {mesero.horas_trabajadas}")
print(f"Total de horas trabajadas en la semana: {restaurante.horas_trabajadas}")

# Calcular salarios
nomina = Nomina(restaurante.meseros)
salarios_meseros = nomina.calcular_salario()

print("Salarios:")
for mesero, salario in salarios_meseros.items():
    print(f"{mesero}: ${salario}")

