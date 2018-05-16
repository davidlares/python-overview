def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() # local
    def mostrar():
        print(mensaje)
    return mostrar # aqui guardamos el print de la funcion

# una funcion genere dinamicamente otra funcion -> esta nueva funcion acceda a la variables locales cuando la primera
# haya finalizado

nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()
