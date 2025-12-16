
class Carro:

    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

 
    def arranque(self):
        return f"{self.modelo} puede arrancar."

    def apagado(self):
        return f"{self.modelo} se apaga correctamente."

    def aceleracion_frenado(self):
        return f"{self.modelo} acelera y frena conforme a lo que se use."

    def sistema_direccion(self):
        return f"{self.modelo} tiene sistema de dirección correcto."

    def climatizacion(self):
        return f"{self.modelo} tiene climatización optima."

    def tipo_seguridad(self):
        return f"{self.modelo} cuenta con un tipo de seguridad confiable."

    def luces(self):
        return f"{self.modelo} las farolas funcionan bien."

    def sistema_ventanas(self):
        return f"{self.modelo} permite subir y bajar ventanas."

    def sistema_espejo(self):
        return f"{self.modelo} tiene espejos."

   
    def asignar_atributos(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible