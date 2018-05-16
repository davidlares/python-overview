animal = "Delfin" # variables globales (fuera de la funcion)
def mostrar_animal(): # cada funcion contexto - namespace (pueden coexistir)

    #forzamos el llamado a la variable global
    global animal # por lo que global es Ballena tambien

    animal = 'Ballena' # la variable es local
    print(animal)
mostrar_animal()
print(animal)
