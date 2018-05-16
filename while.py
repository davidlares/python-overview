numero = 12345678
contador = 0

while numero >= 1:
    contador += 1
    numero = numero / 10
else: # cuando la condicion no se cumple
    print("La cantidad de digitos del numero es: ", contador)
