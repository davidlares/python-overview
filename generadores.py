# Generadores -> tipo especial de funcion para generar una secuencia de datos (a iterar)
# la secuencia retornada, no se va a definir, no se va a almacenar en mem RAM

def tabla_multiplicar(numero, max=10):
    for pos in range(1,max + 1): # +1 porque el ultimo no se incluye
        yield numero * pos, numero, pos # retorna el resultado sin terminar la ejecucion de la funcion

for resultado, num, pos in tabla_multiplicar(9):
    print(resultado,"*", pos, "=", resultado)

# las funciones terminan -> ejecutando la ult linea de codigo o lo que venga con return
