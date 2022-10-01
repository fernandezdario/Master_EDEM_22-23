#RETO 1
name = 'Darío'
apellidos = 'Fernández Fernández'
age = int(22)
email = 'ferrnandezdario17@gmail.com'
teleph = int(638593606)
casado = True
con_hijos = False
lista_amigos: (str) = ['Dani', 'Jaime', 'Ignacio', 'Salva']
Peliculas_Vistas = {
  "Mejor pelicula": "Interstellar",
  "Pelicula más divertida": "Ali G",
  "Mas lacrimogena": "Your name"
}
print(name, apellidos, age, email, teleph, casado, con_hijos, lista_amigos, Peliculas_Vistas)


#RETO 2
RangoImpar = range(1,8,2)
print(*RangoImpar)


#RETO 3
lista1_100 = range(1,101)
orden_inverso = reversed(lista1_100)
print(*orden_inverso)


#RETO 4
lista_original = [1,2,3,4,5]
lista_revertida = reversed(lista_original)
print(*lista_revertida)


#RETO 5
'''Esta primera alternativa es sin generar un bucle, de tal forma que si te equivocas en la contraseña tendrás que volver a iniciar el proceso.'''
user_ = 'Dario'
passwd = 'admin'
print('Bienvenido, ingrese sus datos')
user = input('Nombre de usuario:')
contraseña:str = input('Introduzca su contraseña:')
if user==user_ and contraseña==passwd:
    print('Bienvenido al programa señor ADMIN!')
else:
    print('Usuario o contraseña inválidos. Por favor vuelva a introducir los datos correctamente.')


'''En esta segunda alternativa, entramos en un bucle en cuanto no introducimos la contraseña correcta, de tal forma que el programa nos insistirá
de forma indefinida que introduzcamos la contraseña correcta, hasta que finalmente lo hagamos.'''
print('Bienvenido al sistema!')
user_ = 'Dario'
user = input('Escribe tu usuario: ')
contraseña = 'admin'
password:str = input('Introduce una contraseña: ')
while password != contraseña:
    print('La contraseña no es correcta.')
    password = input('Inténtalo otra vez:')

print('Bienvenido al programa señor ADMIN!')


#RETO 6
age = int(input('Escribe tu edad:'))
if age < 18 :
    print('Eres menor de edad.')
else:
    print('Eres mayor de edad.')


#RETO 7
'''Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. 
El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas'''

contraseña_usuario = 'password de prueba'
pswd:str = input('Escriba su contraseña aquí:')
if contraseña_usuario==pswd:
    print('El texto introducido coincide.')
else:
    print('El texto intrducido es diferente.')

#RETO 7
'''Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. 
El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas
En esta alternativa si que se distingue entre mayúsculas y minúsculas, de tal forma que si escribimos el texto tal cual lo hemos escrito en la
variable, nos arrojará que el texto coincide. Sin embargo, si alguna de las letras cambia a mayúscula o minúsucla nos dirá que el texto es diferente.'''
contraseña_usuario = 'password de prueba'
pswd:str = input('Escriba su contraseña aquí:')
if contraseña_usuario==pswd:
    print('El texto introducido coincide.')
else:
    print('El texto intrducido es diferente.')

#Alternativa 2

'''passwd_user = 'hello'
contra:str = input('Escribe la contraseña aquí:')
print(passwd_user is contra)
'''

str1 = 'Mark'
str2 = str1
str3 = 'MARK'
print(str1 is str2)
print(str1 is str3)

'''https://www.youtube.com/watch?v=5XaaP1b3yhM&ab_channel=Dimas min 3:15
De esta manera podremos saber son diferentes independientemente de si hay mayusculas o minisculas.'''

#RETO 8
'''Escribe un programa que pueda decirte si un número (número entero) es primo o no'''
'''https://geekflare.com/es/prime-number-in-python/'''


#Reto 13: Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo
import math

def reto13():
    base = int(input('Escribe la base del triángulo: '))
    height = int(input('Escribe la base del triángulo: '))
    radius = int(input('Escribe el radio del circulo: '))
    def areaTriangle(a: int, b: int):
        return (a * b * 0.5)
    print(f' El area del triángulo es : {areaTriangle(a = base, b = height)}')
    def areaCircle(r: int):
        return (math.pi * r**2)
    print(f' El area del circulo es: {areaCircle(r = radius)}')

#Reto 14: Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
#Volumen de un cilindro:

import math
radius = int(input('Escribe el radio del circulo: '))
altura = int(input('Escribe la altura del cilindro: '))
def areaCircle(r: int):
    return (math.pi * r**2)
print(f'El area del circulo es: {areaCircle(r = radius)}')
areaCirculo = areaCircle(r = radius)
def reto14():
  def volCilindro(areaCirculo: int, h: int):
    return (areaCirculo * h)
  print(f'El volumen del cilindro es: {volCilindro(areaCircle, h = altura)}')

#alternativa
from Retos.Reto13 import areaCircle  

def Reto14():
  def volCilindro(radius: float, altura: float) -> float:
    base: float = areaCircle(radius)
    volumen = float(base) * float(altura)
  return print(volumen)

  #afdasfdasf

import math

def reto14():
  radius = int(input('Escribe el radio del circulo: '))
  altura = int(input('Escribe la altura del cilindro: '))
  def areaCircle(r: int):
    print(f'El area del Circulo es {areaCircle(r = radius)}')
    return (math.pi * r **2)
  def volCilindro(r: float, h: float) -> float:
    print(f'El volumen del cilindro es: {volCilindro(r = radius, h = altura)}')
    return areaCircle(r) * h


'''Reto 17
Partiendo de la siguiente tupla:
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Realiza las siguientes operaciones:
- Encontrar los elementos de 3 a 5 
- Encontrar los 6 primeros elementos
- Muestra la tupla desde el 5 elemento hasta el final
- Muestra toda la tupla haciendo uso de [:]
- Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
- Devuelve la tupla con un salto cada 4 elementos
- Usa un step negativo para mostrar la tupla desde la posición 9 a la 2'''

def reto17():
  tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
  print(tupla [2:5])
  print(tupla [:6])
  print(tupla[4:])
  print(tupla [:])
  print(tupla[1:9:2])
  print(tupla[0:9:4])
  print(tupla [9:1:-1])