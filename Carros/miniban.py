
from carro_padre import Carro

class Miniban(Carro):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def capacidad_carga(self):
        return f"{self.modelo} está diseñada para servicio publico."

    def sistema_ventanas(self):

        return f"{self.modelo} tiene ventanas manuales para el uso de los pasajeros."
