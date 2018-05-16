# funciones sin parametros definidos
def suma(required, *args):
# def suma(v1,v2,v3):
    total = 0
    for valor in args:
        total += valor
    return total
    # return v1 + v2 + v3
resultado = suma("Arg requerido",1,2,3)
print(resultado)

def usuarios_autenticados(**kwargs): # cantidad de argumentos
    # convencion **kwargs -> convierte todo en parametros en un diccionario usando los parametros
    print(kwargs)

usuarios_autenticados(codi=True, facilito=False)
