class Restaurante:

    def __init(self):

        pass

    def registrar_mesero(self, nombre: str):
        self.nombre: str = nombre

    def descanso(self, dias_descanso: str):
        self.dias_descanso: str = dias_descanso

    def dias_laborales(self, dias_laborados: str):
        self.dias_laborados: str = dias_laborados

    def meseros(self, num_meseros: int):
        self.num_meseros: int = num_meseros


class Mesero:

    def __init__(self, nombre: str, documento: int, correo: str):
        self.nombre: str = nombre
        self.documento: int = documento
        self.correo: str = correo
