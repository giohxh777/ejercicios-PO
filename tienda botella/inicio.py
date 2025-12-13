from modelo_botella import Botella # type: ignore
from modelo_botella_hija1 import Botella_plastico # type: ignore
from modelo_botella_hija2 import Botella_vidrio # type: ignore

#codigo principal
botella_plastico = Botella_plastico("plástico", "500ml", "cilíndrica", "normal", "si", "ninguno")
print(" BOTELLA PLÁSTICO")
print(f"Material: {botella_plastico.material}")
print(botella_plastico.compatible_bebidas_calientes())
print("la botella tiene las siguientes caracteristicas: material:", botella_plastico.material, ", capacidad:", botella_plastico.capacidad, ", forma:", botella_plastico.forma, ", diseño:", botella_plastico.diseño, ", tapa:", botella_plastico.tapa, ", grabados:", botella_plastico.grabados)

botella_vidrio = Botella_vidrio("vidrio", "750ml", "cilíndrica", "elegante", "si", "grabados")
print(" BOTELLA VIDRIO")
print(f"Material: {botella_vidrio.material}")
print(f"Capacidad: {botella_vidrio.capacidad}")
print(botella_vidrio.compatible_bebidas_calientes())
print("la botella tiene las siguientes caracteristicas: material:", botella_vidrio.material, ", capacidad:", botella_vidrio.capacidad, ", forma:", botella_vidrio.forma, ", diseño:", botella_vidrio.diseño, ", tapa:", botella_vidrio.tapa, ", grabados:", botella_vidrio.grabados)

