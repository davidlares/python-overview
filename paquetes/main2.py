# archivo que contiene codigo PY, permite reutilizar codigo de distintos proyectos
# from calc import *
from calc import (suma, resta, div, mult)
# el nombre del modulo = nombre de archivo para importar (no haria falta poner el llamado al modulo)
resta = resta(10,2)
print(resta)

mult = mult(10,2)
print(mult)

div = div(10,2)
print(div)

# se le pueden poner alias -> from calc import suma as ALIAS
