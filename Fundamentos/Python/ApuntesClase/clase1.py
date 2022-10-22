'''este es un comentario
especilamente largo'''
print("Hola Mundo")

user = "Darío"
print("Hola" + " " + user)

user = "Alba"
print("Hola" + " " + user)

user = 200
user = user * 2
print (user)

NewUser:str = "Pepe"
NewUser = 3
print(NewUser)

user = "Juan"

bienvenida = f"Hola {user}"

print(f'''{bienvenida}, 
tu numero de usuario es {NewUser}''')
#tambien se puede poner \n para introducir salto de linea

'''
bool: True or False
str: cadena de texto
int: entreros
float
complex: numeros complejos
list [.....]
tuple (..., ...,...)
dict {key: value, key: value...)
set: No se duplican valores
frozen set: no se puede modificar, no es variable
bytes: representar en bytes los valores
range
'''


'''
BOOL
'''
casado: bool = True
print(f'Casado? {casado}')




'''LISTA'''

miLista: (str) = ['Martin', 'Juan', 'Pablo']

print(miLista)
print(*miLista)
#cuando le pones el asterisco te hace una iteración por los valores, de forma que te deja la lista completamente limpia

print(miLista[1])
#cuando le indica el 1 sabe que posicion quires coger de la lista, ya que el primer valor (Martín) sería el 0.

'''
lISTA
'''

lista_compra = ["tomate", "lechuga", "agua", "vodka", "vasos"]

print(lista_compra[3], "y", lista_compra[4])
#este ejemplo solo sirve para esta lista ya que solo coge los dos últimos elementos de ESTA lista, pero si añades más elementos no cogería los dos últimos elementos porque solo cogería esas posiciones.

print(lista_compra[-1], lista_compra[-2])
#si en vez de hacerlo con números enteros positivos, lo hacemos con negativos nos cogerá los últimos elementos de la lista, de esta forma podemos reutilizarlo y no realizarlo varias veces. 

print(*lista_compra[-2:])
#de esta forma digo que desde el penultimo elemento hasta el final que me liste los elementos que hay, es decir el penúltimo y el último, de esta forma con los : dices que si hay valores infinitos que coja los elementos hasta el infinito. 

lista_compra[2:10:1]
#de esta forma le dices que vaya desde el elemento dos hasta el elemento 10 en saltos de 1 en 1. 

'''
RANGOS
'''

miRango = range(0,11,2)
print(*miRango)
#debemos poner el 11, ya que si ponemos el 10 no nos lo cogería 
#si no le ponemos el * lo convertirá directamente a texto y si queremos los valores que entran dentro del rango, lista, diccionario... debemos ponerlo. 

esPar = 3%2
#de esta forma podemos comprobar si un número es par

'''
Diccionario
'''

persona = {
  "nombre": 'pepo',
  "edad": 28,
  "DNI": "6348274K",
  "casado": True
}

print(persona['DNI'])
print(f"El DNI de {persona['nombre']} es {persona['DNI']}")

'''
SET
'''

misNumeros = [1,2,3,4,5,6,7,8,9,3,2,5,3]
misNumerosNoduplicados = set(misNumeros)
print(misNumerosNoduplicados)

miOtrosetdedatos = set(["a", "a", "a", "b"])
print(*miOtrosetdedatos)

#como ordenar listas
listaxd = [3,1,8,2,9,10,7]
listaordenada = sorted(listaxd)
print(*listaordenada)

#como invertir listas
listainvertida = reversed(listaxd)
print(*listainvertida)

#paso por 'valor'
#paso por 'referencia'

name = input('Dime tu nombre: ')
edad = int(input("Cual es tu edad?"))
print(f"Hola: {name}. Tienes {edad} años")

#si quiero pasar de un texto a un numero debemos usar una función (int)

'''Ejercicio: 
Hacer aplicacion de consola, pidiendo:
nombre
email
contrseña
edad
aceptar
Es decir creando un diccionario usuario'''




puntos_obtenidos: int = 0
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
puntos_obtenidos += 1
print(f"> Has conseguido otro punto. Ahora tienes: {puntos_obtenidos}")

