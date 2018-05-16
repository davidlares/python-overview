diccionario = {'a': 1, 'b': 2,'c': 3,'d':4}
# llaves
llaves = diccionario.keys()
print(llaves)
print(list(llaves))

# convert
values = diccionario.values()
print(values)
print(tuple(values))
# se pueden convertir en listas o tuplas

# items
items = diccionario.items()
print(items)
print(list(items))

# eliminar una llave
del diccionario["a"]
diccionario.pop("b")
print(diccionario)

diccionario.clear()
print(diccionario)
