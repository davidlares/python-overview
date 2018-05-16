tupla = (1,2,3,4)
# uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]
uno, dos, tres, cuatro = tupla
print(uno)
print(dos)
print(tres)
print(cuatro)

# las tuplas y las variables deben tener la misma cantidad de elementos
uno, dos, tres, *cuatro = tupla
print(uno)
print(dos)
print(tres)
print(cuatro)

# operaciones
lista = [10,20,30,40]
# generar nuevas tuplas
resultado = zip(tupla, lista) # regresa objeto de tipo ZIP
print(resultado)
# convertir en tupla -> metodo Tuple
resultado = tuple(resultado)
print(resultado)

# convertir en lista

resultLista = list(resultado)
print(resultLista)
