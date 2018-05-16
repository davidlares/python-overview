class Usuario: # las clases son en camelcase

    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.email = correo
        self.nombre = nombre

    def saluda(self): # parametro ajuro (self no es una palabra reservada)
        return "Hola, soy " + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    # def crear_nombre(self,nombre):
    #     self.nombre = nombre

david = Usuario('davidlares','david@gmail.com','David') # realizar una instancia
resultado = david.saluda()
print(resultado)
# david.username = 'david'
# david.email = 'david@gmail.com'

# print(david)
# print(david.saluda("Usuario David"))
