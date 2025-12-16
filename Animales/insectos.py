from animales_padre import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return f"{self.nombre} camina y puede volar cortas distancias."

    def alimentarse(self):
        return f"{self.nombre} se alimenta de plantas ."