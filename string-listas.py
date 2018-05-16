lenguajes = "Python; Java; Ruby; PHP"
# metodo split y join
resultado = lenguajes.split("; ") # genera una lista
print(resultado)

string = " ".join(resultado) # genera un string
print(string)

texto = """ Este es un
texto
con saltos
de
linea
"""

final = texto.splitlines()
print(final)
