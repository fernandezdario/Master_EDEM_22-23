'''Palabras reservadas de python
Se trata de algunas palabras que no podemos utilizar para nombrar variables
- and: sirve para concatenar condiciones
- as: sire para tratar valores de distintos tipos de una manera o de otra
- assert:
- break: sirve para interrumpir un proceso o cuando ocurra algo especifico se termine la operación
- class: palabra para declarar tipos propios, una clase te permite crear objetos también
- continue: si en determinados queremos que una acción continue utilizamos esta palabra
- def: sirve para definir una función, es una manera de definir unas lineas de código definidas por un ambito para poder reutilizar lineas de código y que sea mas sencillo escribir codigo
- del:
- elif: se trata de un if + else, se utiliza para definir más condiciones
- else:
- except:
- exec:
- finally: si queremos que algo se ejecute si o si, se utiliza esta palabra
- for: itera por cada uno de los elementos de la lista
- global: es para definir variables de un ambito superior
a = 0
nombre = 'pepe'
if a==0:
  nombre ='martin' este es un nuevo ámbito
print(nombre)
En este caso se imprime martín porque le das un nuevo valor a la variable

- if:
- import: podemos importar lo que necesitemos
- in: dentro de, normalmente en una lista o en aquello que sea iterable
- is: para saber si un valor es de diferentes tipos o si cumple determinadas condiciones
- lambda:
- nonlocal:
- not: 
- or: o uno o el otro
a = 1
b = 2
if (a == 0 and b == 2) or a ==1:
  name = 'martin'
print(name)
aqui imprimiria martin por que la condicion de a == 1 despues del or si que se cumple. Sin embargo, si la primera se cumple, la maquina ya no buscaria la condicion de después del or

- pass: por ejemplo que se salte una iteración
- raise:
- return: 
def: suma (a,b):
  return a + b

valor1 = suma(1,2)
valor2 = suma(5,9)
print(valor1, valor2)
Esto se utiliza para reutilizar código, ya que la suma siempre sumará los valores de las variables que luego le des.

- try: se utiliza para gestionar los errores y las excepciones
- while: es una de las maneras para hacer un bucles, mientras que esta condicion se cumple ejecuta esto, y lo que puede pasar es que se produzca un bucle infinito
- with:
-yield: sirve para emitir valores y trabajar con procesos asincronos
- True: aqui es lo mismo que un 1
- False: y none son lo mismo al igual que el 0
- none:

Ejercicio investigar la utilidad de las palabras reservadas y ponerlo con nuestras palabras
'''


'''
numeroElegido = int(input('Elige un número: '))

while(numeroElegido%2 == 0): #aqui siempre que la condicion de que el numero sea par el bucle siempre te pedira que elijas el numero
  numeroElegido = int(input('Elige un número: '))

while(numeroElegido%2 != 0): #aqui es con numeros impares
  numeroElegido = int(input('Elige un número: '))

'''

numeroElegido = int(input("Elige un número: "))
numeroBuscado = 300
intentos = 3

'''
while(numeroElegido % 2 != 0):
  numeroElegido = int(input("Vuelve a elegir un número: "))
'''

while(numeroElegido != numeroBuscado):
  if(numeroElegido > numeroBuscado):
    numeroElegido = int(input("Has fallado, el número buscado es más pequeño: "))
  else:
    numeroElegido = int(input("Has fallado, el número buscado es más grande: "))

print(f"Has ganado, el número era {numeroBuscado}")









'''EJ
Por consola el usuario debe acertar un numero secreto, tiene 3 intentos, si acierta en el primer intento, tus puntos se multiplican por 2 y se suman 5 puntos
si acierta en el segundo intento se suman 5 puntos
si acierta a la tercera se suman 2 puntos
si falla todas las veces se restan 2 puntos '''

'''a = 1
b = 2
c = 3
name = "pepe"

if (a == 0 and b == 2) and c == 3:
  name = "martin"
  print(name)

def suma (primer, segundo):
  return primer + segundo

valor1 = suma(1,2)
valor2 = suma(5,9)
valor3 = suma(-2, -10)
valor4 = suma(1,2) + suma(4,5)
# print(valor1, valor2, valor3, valor4, suma(4,4))
suma(5,6)


while(a == 3):
  print("yeah")
  a = 2


numeroElegido = int(input("Elige un número: "))
numeroBuscado = 300
intentos = 3

'''
while(numeroElegido % 2 != 0):
  numeroElegido = int(input("Vuelve a elegir un número: "))
'''

while(numeroElegido != numeroBuscado):
  if(numeroElegido > numeroBuscado):
    numeroElegido = int(input("Has fallado, el número buscado es más pequeño: "))
  else:
    numeroElegido = int(input("Has fallado, el número buscado es más grande: "))

print(f"Has ganado, el número era {numeroBuscado}")

operacion_compleja = 33 * 10 + 2 / 5 ** 2
print(f"> Operación 33*10+2/5**2 = {operacion_compleja}")


nombre: str = "Martín"
apellidos: str = "San José de Vicente" 

# Concatenación
nombre_completo: str = nombre + " " + apellidos
print(f"> Nombre completo: {nombre_completo}")  

# Repetición
nombre_x5: str = nombre*5
print(f"> Nombre 5 veces: {nombre_x5}")

c: int = 3
d: int = 3
e: int = 4

# Igualdad - Nos devolverá True o False
print(f"> ¿3 y 3 son iguales? {c is d}") 
# Operador Identidad
print(f"> ¿3 y 3 son iguales? {c == d}")
print(f"> ¿3 y 4 son iguales? {c is e}") # Operador Identidad


print(f"¿3 mayor que 2? {3 > 2}")



print(f"Verdadero y Verdadero = {True and True}")
print(f"Verdadero y 1 = {True and 1}")
print(f"> Falso y 0 = {False and 0}")

	
print(f"Not Verdadero = {not True}")
print(f"Not Falso = {not False}")
print(f"Not Falso o Verdadero = {not (False or True)}")

mi_texto:str = "Lorem ipsum dolor sit amet consectetur adipiscing elit dui odio"
mi_sub_texto: str = "amet"
mi_otro_sub_texto: str = "pepito"

print(f"> ¿amet está dentro del mi_texto?: {mi_sub_texto in mi_texto}")
print(f"> ¿pepito no está dentro de mi_texto?: {mi_otro_sub_texto not in mi_texto}")

edad = 30
edad += 1


puntos_obtenidos: int = 0
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
puntos_obtenidos = puntos_obtenidos + 1
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
puntos_obtenidos += 1
print(f"> Has conseguido otro punto. Ahora tienes: {puntos_obtenidos}")




EJERCICIO
- Por consola el usuario debe acertar un número secreto
- Tiene 3 intentos
- Si acierta en el primer intento: Se suman 5 puntos y el resultado se multiplican por 2
- Si acierta en el segundo intento: Se suman 5 puntos
- Si acierta a la tercera: Se suma 2 puntos
- Si falla todas las veces: Se resta 2 puntos


'''