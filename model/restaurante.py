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

    def semana(self,dias_semana):
        self.dias_semana: list= ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

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

    def dias_laborales(self, dias_laborados: str):
        self.dias_laborados: str = dias_laborados




