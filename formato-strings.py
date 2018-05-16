texto = "curso de Python 3"
cap = texto.capitalize() # nuevo string
print(cap)

swap = texto.swapcase() # de mayus a minus, y viceversa
print(swap)

upper = texto.upper() # todo a mayus
print(upper)

lower = texto.lower() # todo a minus
print(lower)

print(texto.isupper())
print(texto.islower())

# metodo title
tit = texto.title()
print(tit)

# metodo replace
rep = texto.replace("Python","Ruby", 1) #times number
print(rep)

# metodo strip -> quita espacios en blanco
strip = texto.strip()
print(strip)

# sin metodos
curso = "Python"
version = "3"
sm = "Curso de %s %s" %(curso,version)
# %s reemplazo por posicion -> S de String
# metodo format
form = "Curso de {} {}".format(curso,version)
form2 = "Curso de {a} {b}".format(a=curso,b=version)
# opcional los datos, mover los valores es mejor, sino tednria que ser de forma ordenada
print(sm)
print(form)
print(form2)

# concatenacion
