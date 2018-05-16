# metodos parecidos a los estaticos, llamables sin hacer instancia de la clase
class Circulo:
    pi = 3.14 # variable de clase

    @classmethod #  decoramos para que sea un metodo de clase
    def area(cls,radio): # deben recibir un parametro por defecto (cls) -> por convencion
        return cls.pi * radio**2

resultado = Circulo.area(10)
print(resultado)
