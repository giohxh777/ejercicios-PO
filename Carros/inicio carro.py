from carro_padre import Carro
from miniban import MiniVan
from carro_deportivo import Deportivo
from camion import Camion



Deportivo_bmw = Deportivo("BMW ", "negro", "combustion de 3L", 2, 2, "Gasolina")
miniban = MiniVan("Mini Van", "Blanco con azul", "combustion de 2L", 4, 8, "Gasolina")
Camion_ = Camion("camion de carga", "blanco", "Diesel de 6L ", 2, 2, "Diesel")

vehiculos = [Deportivo_bmw, miniban, Camion_]

for v in vehiculos:
    print(f"\nVEHÍCULO: {v.modelo}")
    print(f"Color: {v.color}, Motor: {v.motor}, Puertas: {v.num_puertas}, Capacidad: {v.capacidad_pasajeros}, Combustible: {v.tipo_combustible}")
    print(v.arranque())
    print(v.aceleracion_frenado())
    print(v.sistema_direccion())
    print(v.climatizacion())
    print(v.tipo_seguridad())
    print(v.luces())
    print(v.sistema_ventanas())
    print(v.sistema_espejo())