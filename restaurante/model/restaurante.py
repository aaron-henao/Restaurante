import random

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


class Mesero:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.dias_descanso = 0
        self.horas_trabajadas = 0
        self.dia_descanso_personalizado = None

    def asignar_descanso_personalizado(self, dia_descanso: str):
        self.dia_descanso_personalizado = dia_descanso

    def tiene_dia_descanso_personalizado(self, dia: str):
        return self.dia_descanso_personalizado == dia


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
                max_meseros_descanso = 3  # Hasta tres meseros pueden tener un día libre durante estos días
            else:
                max_meseros_descanso = 2  # Dos meseros pueden tener un día libre en los otros días

            meseros_descanso = []
            meseros_cierre = []  # Meseros asignados al turno "12:00 pm - cierre" para garantizar que el restaurante
            # nunca quede desatendido

            # Verificar si hay día de descanso personalizado para el mesero
            for mesero in meseros_disponibles:
                if mesero.tiene_dia_descanso_personalizado(dia):
                    meseros_descanso.append(mesero)
                    mesero.dias_descanso += 1

            # Asignar descanso aleatorio si no se ha asignado uno personalizado
            if len(meseros_descanso) < max_meseros_descanso:
                for _ in range(max_meseros_descanso - len(meseros_descanso)):
                    mesero_descanso = random.choice(meseros_disponibles)
                    meseros_descanso.append(mesero_descanso)
                    mesero_descanso.dias_descanso += 1

            for mesero in meseros_disponibles:
                if mesero in meseros_descanso:
                    horarios[dia].append(mesero.nombre + ": Descanso")
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

