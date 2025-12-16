from carro_padre import Carro


class Camion(Carro):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)

    def capacidad_carga(self):
        return f"El {self.modelo} está diseñado para transportar grandes cargas."

    def sistema_frenos(self):
        return f"El {self.modelo} cuenta con un sistema de frenos reforzado para mayor seguridad."