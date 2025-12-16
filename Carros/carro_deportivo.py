
from carro_padre import Carro

class Deportivo(Carro):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def aceleracion_frenado(self):
        return f"El {self.modelo} tiene gran potencia de aceleracion y frenado eficiente a altas velocidades."

    def tipo_seguridad(self):
        return f"El {self.modelo} cuenta con equipamento protector y frenos de disco."