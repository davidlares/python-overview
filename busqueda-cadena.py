mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
resultado = mensaje.count("texto") # busqueda bajo un criterio
print(resultado)

# resumido - booleano
otraforma = "texto" in mensaje # booleano
print(otraforma)

# metodo find
encontrar = mensaje.find("texto")
print(encontrar)

# no encuentra nada, retorna un -1

# startswith
principio = mensaje.startswith("Este")
print(principio)


# endswith
final = mensaje.endswith("Este")
print(final)
