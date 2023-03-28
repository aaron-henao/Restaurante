import random


class Restaurante:

    def __init(self):

        pass

    def registrar_mesero(self, nombre: str):
        self.nombre: str = nombre


    def mesero(self, num_meseros: int):
        self.num_meseros: int = num_meseros


class Mesero:

    def __init__(self, nombre: str, documento: int):
        self.nombre: str = nombre
        self.documento: int = documento

    def mesero(self, meseros: list):
        self.meseros: list = []


class Horarios:
    HORAS_MAXIMAS = 48
    def __init__(self, documento: Mesero.documento,dias_descanso, horas: int):
        self.documento: Mesero.documento = documento
        self.dias_descanso: str = dias_descanso
        self.horas: int = horas

    def semana(self,dias_semana: list):
        self.dias_semana: list = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

    def horario_restaurante(self, horario_servicio:list, horario_almuerzo: tuple, horario_tarde: tuple, horario_cena: tuple):
        self.horario_servicio: dict = {
            'lunes': (11, 22),
            'martes': (11, 22),
            'miércoles': (11, 22),
            'jueves': (11, 22),
            'viernes': (11, 23),
            'sábado': (11, 23),
            'domingo': (11, 22),
        }
        self.horario_almuerzo: tuple = (12,15)
        self.horario_tarde: tuple = (15,18)
        self.horario_comida: tuple = (18, 23)

    def descanso(self, dias_descanso: str):
        self.dias_descanso: str = dias_descanso
        for i in range (self.num_meseros):
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




