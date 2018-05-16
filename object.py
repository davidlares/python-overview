class Gato:
    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre # este metodo __str__ va a permitir sobreescribir el mensaje cuando se imprime
        #un objeto completo en consola, evita sacar la memoria

class Pato(object):
    def __init__(self,nombre):
        self.nombre = nombre

# ambos casos herendan de object
gato = Gato("Bigote")
pato = Pato("Lucas")
print(gato)
print(pato)

# metodos de la clase object __ nombre __

# detectar atributos __dict__
print(gato.__dict__)
