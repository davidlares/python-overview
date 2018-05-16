def crear_usuario(n,a,e=5): # el valor por default omite el elemento, la asignacion no debe tener espacios
    return {
        'nombre': n,
        'apellido':a,
        'nombre_completo': "{} {}".format(n,a),
        'edad': e
    }

codi = crear_usuario(n="David",a="Lares") # al identificarlo no hay pele (sin importar el orden)
print(codi['nombre'])
print(codi['apellido'])
print(codi['edad'])
