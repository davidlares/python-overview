import calc

# animales (paquete) aves (modulo) import CLASE
# from animales.aves import Pinguino
from animales import Pinguino, mi_jaguar # eso pasa porque espefique en el init, el llamado al import de la clase Aves
print(calc.__name__)
print(__name__) # __main__ -> todos los archivos principales tienen el metodo __main__ (punto de entrada)

# instancia
pinguino = Pinguino()
pinguino.nadar()

# se importa la instancia y se usa
mi_jaguar.cazar()
