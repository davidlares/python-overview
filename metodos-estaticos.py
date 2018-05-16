# metodos sin la necesidad de una instancia
class Triangulo:

    # metodo de instancia, porque usan self
    # def area(self):
    #     return (self.base * self.altura) / 2

    @staticmethod
    def area(base,altura):
        return(base * altura) / 2

# METODOS INSTANCIA
# t = Triangulo()
# t.base = 10
# t.altura = 20
# resultado = t.area()
# print(resultado)

# METODO ESTATICO
resultado = Triangulo.area(10,20)
# al usarlo, no debemos tener metodos de instancia
