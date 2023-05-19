import tkinter as tk
from tkinter import ttk
import random

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


class Mesero:
    def _init_(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.dias_descanso = 0
        self.horas_trabajadas = 0
        self.dia_descanso_personalizado = None

    def asignar_descanso_personalizado(self, dia_descanso: str):
        self.dia_descanso_personalizado = dia_descanso

    def tiene_dia_descanso_personalizado(self, dia: str):
        return self.dia_descanso_personalizado == dia
#REQUISITO #5 - Notificación diaria
    def enviar_correo(self, dia: str, turno: str):
        mensaje = f"Hola {self.nombre}, tu turno para el día {dia} es: {turno}."
        # Aquí puedes implementar la lógica para enviar el correo al mesero utilizando su dirección de correo electrónico
        print(f"Enviando correo a {self.correo}: {mensaje}")


class Restaurante:
    def _init_(self):
        self.meseros = []
        self.horas_trabajadas = 0
#REQUISITO #1 - Agregar mesero
    def agregar_mesero(self, nombre: str, correo: str):
        mesero = Mesero(nombre, correo)
        self.meseros.append(mesero)
#REQUISITO #2 - Generar horarios
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
                max_meseros_descanso = 3
            else:
                max_meseros_descanso = 2

            meseros_descanso = []
            # REQUISITO #3 - Asignar dias de descanso
            for mesero in meseros_disponibles:
                if mesero.tiene_dia_descanso_personalizado(dia):
                    meseros_descanso.append(mesero)
                    mesero.dias_descanso += 1

            if len(meseros_descanso) < max_meseros_descanso:
                for _ in range(max_meseros_descanso - len(meseros_descanso)):
                    mesero_descanso = random.choice(meseros_disponibles)
                    meseros_descanso.append(mesero_descanso)
                    mesero_descanso.dias_descanso += 1

            for mesero in meseros_disponibles:
                if mesero in meseros_descanso:
                    horarios[dia].append(mesero.nombre + ": Descanso")
                    mesero.enviar_correo(dia, "Descanso")
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
                        mesero.enviar_correo(dia, turno)
                    else:
                        horarios[dia].append(mesero.nombre + ": Descanso (Exceso de horas)")
                        mesero.enviar_correo(dia, "Descanso (Exceso de horas)")

            meseros_disponibles = self.meseros.copy()

        return horarios


class Nomina:
    def _init_(self, meseros):
        self.meseros = meseros

    def calcular_salario(self):
        valor_hora = 4830
        salarios = {}
        for mesero in self.meseros:
            salario = mesero.horas_trabajadas * valor_hora
            salarios[mesero.nombre] = salario
        return salarios


def agregar_mesero():
    nombre = nombre_entry.get()
    correo = correo_entry.get()
    restaurante.agregar_mesero(nombre, correo)
    nombre_entry.delete(0, tk.END)
    correo_entry.delete(0, tk.END)


def generar_horarios():
    horarios = restaurante.generar_horarios()
    horarios_textbox.delete(1.0, tk.END)
    for dia, turnos in horarios.items():
        horarios_textbox.insert(tk.END, f"{dia}:\n")
        for turno in turnos:
            horarios_textbox.insert(tk.END, f"- {turno}\n")

#REQUISITO #8 - Hacer pagos
def calcular_salarios():
    nomina = Nomina(restaurante.meseros)
    salarios = nomina.calcular_salario()
    salario_textbox.delete(1.0, tk.END)
    for mesero, salario in salarios.items():
        salario_textbox.insert(tk.END, f"{mesero}: ${salario}\n")


def mostrar_horas_semanales():
    horas_semanales_textbox.delete(1.0, tk.END)
    horas_semanales_textbox.insert(tk.END, f"Total de horas semanales trabajadas: {restaurante.horas_trabajadas}")

#REQUISITO #9 - Puntaje del código
def cerrar_programa():
    puntaje = 0
    while puntaje < 1 or puntaje > 10:
        try:
            puntaje = int(input("Por favor, ingresa un puntaje del 1 al 10 para calificar el código: "))
        except ValueError:
            print("Debes ingresar un número entero del 1 al 10.")

    print("¡Gracias por calificar el código!")
    window.destroy()


# REQUISITO #6 - Menu desplegable
window = tk.Tk()
window.title("Gestión de Horarios y Nómina")
window.geometry("600x400")

# Crear el frame principal
main_frame = ttk.Frame(window, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Crear el frame de entrada de datos
datos_frame = ttk.Frame(main_frame, padding="10")
datos_frame.pack(fill=tk.BOTH, expand=True)

# Crear los widgets de entrada de datos
nombre_label = ttk.Label(datos_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky=tk.W)
nombre_entry = ttk.Entry(datos_frame)
nombre_entry.grid(row=0, column=1)

correo_label = ttk.Label(datos_frame, text="Correo:")
correo_label.grid(row=1, column=0, sticky=tk.W)
correo_entry = ttk.Entry(datos_frame)
correo_entry.grid(row=1, column=1)

restaurante = Restaurante()  # Instancia de la clase Restaurante

agregar_button = ttk.Button(datos_frame, text="Agregar Mesero", command=agregar_mesero)
agregar_button.grid(row=2, column=0, columnspan=2, pady=10)

# Crear el frame de visualización de resultados
resultados_frame = ttk.Frame(main_frame)
resultados_frame.pack(fill=tk.BOTH, expand=True)
#REQUISITO #4 - Mostrar agenda
horarios_label = ttk.Label(resultados_frame, text="Horarios:")
horarios_label.grid(row=0, column=0, padx=10, pady=5)
horarios_textbox = tk.Text(resultados_frame, width=50, height=10)
horarios_textbox.grid(row=1, column=0, padx=10, pady=5)

salarios_label = ttk.Label(resultados_frame, text="Salarios:")
salarios_label.grid(row=0, column=1, padx=10, pady=5)
salario_textbox = tk.Text(resultados_frame, width=30, height=10)
salario_textbox.grid(row=1, column=1, padx=10, pady=5)
#REQUISITO #7 - Mostrar horas trabajadas
horas_semanales_label = ttk.Label(resultados_frame, text="Horas Semanales:")
horas_semanales_label.grid(row=0, column=2, padx=10, pady=5)
horas_semanales_textbox = tk.Text(resultados_frame, width=20, height=10)
horas_semanales_textbox.grid(row=1, column=2, padx=10, pady=5)

acciones_frame = ttk.Frame(main_frame, padding="10")
acciones_frame.pack(fill=tk.BOTH, expand=True)

generar_horarios_button = ttk.Button(acciones_frame, text="Generar Horarios", command=generar_horarios)
generar_horarios_button.pack(side=tk.LEFT, padx=10)

calcular_salarios_button = ttk.Button(acciones_frame, text="Calcular Salarios", command=calcular_salarios)
calcular_salarios_button.pack(side=tk.LEFT, padx=10)

mostrar_horas_semanales_button = ttk.Button(acciones_frame, text="Mostrar Horas Semanales", command=mostrar_horas_semanales)
mostrar_horas_semanales_button.pack(side=tk.LEFT, padx=10)

cerrar_programa_button = ttk.Button(acciones_frame, text="Cerrar Programa", command=cerrar_programa)
cerrar_programa_button.pack(side=tk.RIGHT, padx=10)

scrollbar = ttk.Scrollbar(main_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

horarios_textbox.config(yscrollcommand=scrollbar.set)
salario_textbox.config(yscrollcommand=scrollbar.set)
horas_semanales_textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=(horarios_textbox.yview, salario_textbox.yview, horas_semanales_textbox.yview))

window.mainloop()