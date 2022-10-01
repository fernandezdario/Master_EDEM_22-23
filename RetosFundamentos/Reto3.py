#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso
def reto3():
  lista1_100 = range(1,101)
  orden_inverso = reversed(lista1_100)
  print(*orden_inverso)
  