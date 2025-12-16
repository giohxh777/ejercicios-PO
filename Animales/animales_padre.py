
class Animal :
   
    def __init__(self, dato_nombre, dato_edad, dato_habitad,dato_dieta, dato_tamaño, dato_color):
        self.nombre = dato_nombre
        self.edad = dato_edad
        self.habitad = dato_habitad
        self.dieta = dato_dieta
        self.tamaño = dato_tamaño
        self.color = dato_color
    
      
    def moverse(self):
        return f"{self.nombre} se puede mover."


    def comunicarse(self):
        return f"{self.nombre} se puede comunicar."


    def reproducirse(self):
        return f"{self.nombre} se puede reproducir."


    def alimentarse(self):
        return f"{self.nombre} puede alimentarse."


    def adaptarse(self):
        return f"{self.nombre} esta adaptándose a su entorno."


    def instintos(self):
        return f"{self.nombre} actúa por instinto."


    def descanso(self):
        return f"{self.nombre} está descansando."


    def dormir(self):
        return f"{self.nombre} está durmiendo."


    def interaccion_social(self):
        return f"{self.nombre} interactúa socialmente con otros animales de su especie."
    
    
    def asignacion_caracteristicas(self, dato_nombre, dato_edad, dato_habitad,dato_dieta, dato_tamaño, dato_color):
        self.nombre = dato_nombre
        self.edad = dato_edad
        self.habitad = dato_habitad
        self.dieta = dato_dieta
        self.tamaño = dato_tamaño
        self.color = dato_color
        

        
        
        