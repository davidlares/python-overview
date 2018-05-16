def comenzar_playlist(lista):
    def reproducir():
        nonlocal lista # esta viene siendo la lista de abajo y no la lista de canciones
        lista = [1,2,3]
        for l in lista:
            print(l)
    reproducir() # solo puede ser llamado desde adentro de la funcion
    print(lista) # se pueden modificar las variables locales en funciones anidadas

lista = ['song1','song2','song3']
comenzar_playlist(lista)
