from animales_padre import Animal
from mamiferos import Caballo
from reptiles import Cocodrilo
from peces import Pez
from insectos import Escarabajo
from aves import Pato


caballo = Caballo("Caballo", 7, "Pradera", "pasto", "Grande", "negro")
cocodrilo = Cocodrilo("Cocodrilo", 12, "Rios", "principalmente carne", "Grande", "Verde claro")
pez_tropical = Pez("Pez tropical", 1, "mar, oceano", "algas y microorganismos", "Pequeño", "amarillo")
escarabajo = Escarabajo("Escarabajo", 1.5, "jardines, bosques, maderas   ", "plantas", "Pequeño", "Negro")
pato = Pato("Pato", 5, "Lagos", "migas de pan y plantas", "mediano", "cafe con verde")


animales = [caballo, cocodrilo, pez_tropical, escarabajo, pato]

for animal in animales:
    print(f"ANIMAL: {animal.nombre}")
    print(f"Edad: {animal.edad}, Hábitat: {animal.habitad}, Dieta: {animal.dieta}, Tamaño: {animal.tamaño}, Color: {animal.color}")
    print(animal.moverse())
    print(animal.alimentarse())
    print(animal.comunicarse())
    print(animal.reproducirse())
    print(animal.adaptarse())
    print(animal.instintos())
    print(animal.descanso())
    print(animal.interaccion_social())