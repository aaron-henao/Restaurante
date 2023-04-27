import random
from dataclasses import dataclass
from typing import ClassVar


class Restaurante:

    def __init(self):
        pass

    def registrar_mesero(self, meseros: list[tuple]):
        self.meseros: list[tuple] = meseros[(self.nombre, self.documento)]


@dataclass
class Mesero:
    nombre: str
    documento: int

    def agregar_mesero(self, nombre: str, documento: int):
        self.nombre: str = nombre
        self.documento: int = documento
        Restaurante.registrar_mesero(self.nombre, self.documento)




@dataclass
class Horario:
    DIAS_SEMANA: ClassVar[list[str]] = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
    HORARIO_RESTAURANTE: ClassVar[dict] = dict
    var = {"LUNES": (11, 22),
           "MARTES": (11, 22),
           "MIÉRCOLES": (11, 22),
           "JUEVES": (11, 22),
           "VIERNES": (11, 22),
           "SÁBADO": (11, 22),
           "DOMINGO": (11, 22), }
    TURNO_PARTIDO: tuple = (12, 15, 18, 22)
    SALIDA_TEMPRANO: tuple = (11, 18)
    ENTRADA_TARDE: tuple = (15, 22)
    DESCANSO: ClassVar[list[tuple]] = [("LUNES", "MARTES"), ("MARTES", "MIÉRCOLES"), ("MIÉRCOLES", "JUEVES"),
                                       ("JUEVES", "VIERNES"), ("VIERNES", "SÁBADO"), ("SÁBADO", "DOMINGO"),
                                       ("DOMINGO", "LUNES")]

class Tabla:

    def horario_y_meseros(self, tabla_horario: list, DIAS_SEMANA=None):
        self.tabla_horario: list[[list], [list]] = tabla_horario[[Restaurante.registrar_mesero(self.meseros)], [DIAS_SEMANA]]


    def descanso(self, dias_descanso: str):
        self.dias_descanso: str = dias_descanso
        for i in range(self.num_meseros):
            dias_descanso = random.sample(self.dias_semana, 2)
            self.meseros.append({
                'nombre': f'Mesero {i + 1}',
                'dias_descanso': dias_descanso,
                'horas_trabajo': 0,
                'horario_semana': {},
                'horario_diario': {},
                'horario_descanso': {},
                'correo': f'mesero{i + 1}@restaurante.com'
            })

    def apertura(self):
        for i in self.dias_semana:
            mesero_apertura = random.choice(self.meseros)
            mesero_apertura['horario_semana'][i] = {
                'inicio': self.horario_servicio[i][0],
                'fin': self.horario_servicio[i][1],
                'horas_trabajadas': 0
            }

    def generar_horarios(self):
        for self.mesero in self.meseros:
            dias_descanso = self.mesero['dias_descanso']
            dias_trabajo = [i for i in self.dias_semana if i not in self.dias_descanso]
            horas_trabajo_semana = 0
