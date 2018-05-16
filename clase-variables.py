class Circulo:

    pi = 3.14 # variable de clase (sin self), puede ser utilizadas por las instancias

    def __init__(self,radio):
        self.radio = radio # radio es una variable de instancia

circle1 = Circulo(10)
circle2 = Circulo(20)

print(circle1.radio)
circle2.radio = 100
print(circle2.radio)

# uso de la variable sin instancia
print(Circulo.pi)
