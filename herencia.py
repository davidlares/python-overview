class Animal:
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Durmiendo")
    def comun(self):
        print("Este es un metodo comun")

class Mascota:
    def fecha_adopcion(self,fecha):
        self.fecha_adopcion = fecha

class Gato(Animal, Mascota): # HERENCIA MULTIPLES
    def ronroneo(self):
        print("ronroneo")

class Perro(Animal): # esta es la herencia ->
    def __init__(self,nombre):
        self.nombre = nombre
    def ladrar(self):
        print("Ladrando")
    def comun(self):
        print("Mensaje comun de Perro")
    def dormir(self): #aqui hay un oveerride del metodo en la clase Animal
        print(self.nombre, "esta durmiendo!")
        Animal.dormir(self) # sirve para agregar mas funcionalidad a la clase padre para extenderla
        print("No molestar")

firulais = Perro("Firulais")
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.comun() # el metodo es buscado en su clase principal -> si no existe busca a la clase que hereda

snowball = Gato();
snowball.comer()
snowball.dormir()
snowball.fecha_adopcion("Hoy")
print(snowball.fecha_adopcion)

# el llamado a las clases debe ser consecuente
