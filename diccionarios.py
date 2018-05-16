# alm diferentes tipos de datos
# son mutables, modificar valores y tamanos. no se tienen indices, sino llaves para su acceso
#diccionario = {"total": 55}
diccionario = {}
diccionario["nombre"] = "David"
print(diccionario)
valor = diccionario["nombre"]
print(valor)
diccionario["nombre"] = 80
print(diccionario["nombre"])

# si la llave existe -> se reemplaza, sino lo contrario
dic = {"a": 1, "b": 2, "c": 3, "a": 4}
print(dic)
# en caso de haber una llave duplicada, se toma la ultima

resultado = "z" in diccionario
print(resultado)

resultado2 = diccionario.get("a", "not found") # 2do param (error) de busqueda
print(resultado2)

# metodo setDefault
resultado3 = diccionario.setdefault("v", {})
print(resultado3)
