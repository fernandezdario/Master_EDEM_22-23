'''import math

numero:int = 16

print(f'La raiz de {numero} es {math.sqrt(numero)}')

from math import sqrt, sin, cos 
numero: int = 16  
print(f'La raíz cuadrada de {numero} es {sqrt(numero)}')  #imprime 4.0
print(f'El Seno de {numero} es {sin(numero)}')  #imprime -0.287...
print(f'El Coseno de {numero} es {cos(numero)}') #imprime -0.957...
#En estas lineas de print no tenemos que meterle math. antes de cos o sin o lo que sea porque solamente has importado algunas funcionalidades de la libreria, por lo que ya reconoce que forman parte de la libreria ya importada y no es necesario.
from math import tan as tangente
tangente(300)#Si te pone encima de la funcion te indica en que se mide, en el caso de tangente es de radianes.

#from math import* de esta manera importamos todas las funcionalidades y no necesitas poner math.loquesea, sin embargo no es recomendable esta forma porque puede que nos hagamos un lio que te cagas.'''


from utilidades.kpis import puntuacion
import utilidades.interacciones.cordialidad as frases
from utilidades.interacciones.cordialidad import saludar 
#de esta manera (la de arriba justo) la funcion de saludar que se encuentra en el otro modulo se ejecuta aqui. Delante del modulo tendremos que meter los paquetes y subpaquetes en los que se encuentre.
#saludar('Darío')
#print('Final')
#si en vez de tener un print tenemos un return en la funcion de saludar tendriamos que hacerlo de la siguiente manera, ya que al no tener el print en la funcion del otro modulo debes ponerlo aqui para que aparezca por consola.
#saludo = saludar ('Darío')
#print(saludo)

saludo1 = frases.saludar('Darío')
saludo = saludar('Darío')
print(saludo1) # es lo mismno que print(saludo)
print(f'Puntos obtenidos: {puntuacion(5)}')
