# esto convierte el archivo en un paquete (directorio completo)
# se ejecuta cuando el paquete sea utilizado
from .aves import Pinguino
from .aves import Jaguar
print("Este es un mensaje del archivo init")
# consulta a BD o algo por el estilo se hace aqui

# SE PRESTA PARA SINGLETONS -> una sola instancia e importaciones de la instancia
mi_jaguar = Jaguar()
