# funcion range y enumerate
# range - secuencia de numeros a iterar

# for valor in range(10):
for valor in range(1,10): # el segundo parametro no se toma en cuenta
    print(valor)

# se trabaja tambien con numeros negativos
# tambien se pueden con saltos (1,101,2)
lista = [1,2,3,4,5,6]

# ejemplo con enumerate
for (indice,valor) in enumerate(lista):
    print("indice: " + indice, "valor: " + valor)
