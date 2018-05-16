# asignar una funcion a una variable
def grados(grados):
    return grados * 1.8 + 32

function_variable = grados
resultado = function_variable(32)
print(resultado)

# lambdas o funciones anonimas
mifunc = lambda grados=0 : grados * 1.8 + 32 # todas las lambdas retornan un valor
resultado = mifunc(32)
print(resultado)
