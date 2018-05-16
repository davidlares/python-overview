# objetos iterables = listas, tuplas, strings y los diccionarios
numeros = [1,2,3,4,5,6,7,8,9,10]
for n in numeros:
    print(n)

dic = {'a': 1, 'b': 2}
for llave in dic: # por defecto solo recorren las llaves
    print(llave)

valores = ( (10,20), ["strings", "strings"], (True, False))
for valor,valor2 in valores:
    print(valor,valor2)
