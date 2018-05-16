# modificar funcion existe sin cambiar sus lineas de codigo -> sirve para agregar mas funcionalidad
# a(b) -> c

def decorador(funcion):
    # retornar una funcion anidada
    def nueva_funcion():
        print("Mensaje antes de ejecutar la funcion")
        funcion()
        print("Mensaje ejecutado despues de la funcion por parametro")

    return nueva_funcion

@decorador # este es un decorador con el nombre de la funcion inicial
def funcion_a_decorar():
    print("Esta es una funcion a decorar")

# hacemos el llamado de la funcion a decorador
funcion_a_decorar()
