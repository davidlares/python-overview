lista = [8.17,90,1,5,44,1.32]
print(lista.sort()) # ordenamiento ascendente
print(lista.sort(reverse=True)) # ordenamiento descendente
mayor = lista[0]
print(lista)

# min y max
menor = min(lista)
print(menor)

mayor = max(lista)
print(mayor)

# longitud
longitud = len(lista)
print(longitud)

# find
result = 8.17 in lista
print(result)

# index
indice = lista.index(5)
print(indice)

# find times
cont = lista.count(5)
print(cont)
# 0 -> not found
