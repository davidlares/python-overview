# Listas -> Estructura de datos que permite manejar grandes cantidades de datos
# las listas pueden cambiar tamano en tiempo de ejecucion
lista = ['python','Django','Flask','C','C++','C#','Java','PHP']
print(lista[0])
# indices negativos -> recorrido backwards
print(lista[-3])
# sublistas
sub = lista[0:3] # el 0 se puede omitir
print(sub)
print(lista[4:])
# saltos (3er param)
saltos = lista[1:7:2]
print(saltos)
# reverso
reverse = lista[::-1]
print(reverse)
