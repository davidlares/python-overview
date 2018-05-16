# las funciones son snakeCase
def saluda():
    print("Hola amigo")

saluda()

def crear_mensaje(nombre):
    # print("Hola %s" %(nombre))
    return "Hola %s" %(nombre)

mensaje = crear_mensaje("David")
print(mensaje)

def suma(v1,v2,v3):
    return v1 + v2 + v3

print(suma(1,2,3))

def obtener_curso():
    return "Curso de Python", "Basico", 3

curso, nivel, version = obtener_curso()
print(curso, nivel, version)
