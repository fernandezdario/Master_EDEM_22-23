#en el main.py pondremos lo siguiente para que aparezca por pantalla
from http_Requests.chuck_norris_dice import obtenerChiste

chiste = obtenerChiste()
print('********chistecito*******')
print(chiste)

import requests
def obtenerChiste():
  URL = 'https://api.chucknorris.io/jokes/random'#en mayuscula URL pq es una constante, la API es apartir de jokes, ya que el resto nos daria lo que es la web., ya que la URL base es hasta .io/ y luego el endopint es a partir de jokes
  respuesta = requests.get(url = URL) #de esta manera sabemos cual es el parametro que le hemos pasado
#extraemos los datos en formato JSON
  datos = respuesta.json()
# Obtenemos valor en la clave 'value' del JSON que nos interesa
  frase_chuck: str = datos['value']#aqui ponemos esto porque queremos que la frase de chuck norris sea lo que pone en la URL como value, de esta forma cogemos el valor de la URL que es exactamente el chiste. Si en vez de value, pusiesemos ID nos sacaria el ID de la URL.
  return frase_chuck

#creando una clase, primero atributos y luego los metodos
class Alumno :
    nombre: str 
    email: str
    def __init__(self, n, e): #self hace referencia al propio objeto
        self.nombre = n
        self.email  = e
    def asistir.clase(self, id): #si ponemos alumno1.asistir.clase, entonces ese nuevo alumno tendría el metodo que estamos definiendo ahora
    print(f'{self.nombre}')