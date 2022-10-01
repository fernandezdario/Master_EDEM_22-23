#Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
def reto4():
  lista_original = [1,2,3,4,5]
  lista_revertida = reversed(lista_original)
  print(*lista_revertida)