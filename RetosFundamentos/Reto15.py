'''Reto 15
Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.'''


lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [n**2 for n in lista1]#con esta lista lo que hacemos es que cada numero de la lista 1(n) se eleve al cuadrado, es decir, por cada numero existente en la lista 1, cada uno de estos se eleva al cuadrado.
print(lista2)
