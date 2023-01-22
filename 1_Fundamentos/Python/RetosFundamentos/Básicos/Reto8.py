#Escribe un programa que pueda decirte si un número (número entero) es primo o no
def reto8():
  numeroPedido = int(input('Escribe tu número y te diré si es primo: '))
  for n in range(2, numeroPedido):
    if (numeroPedido % n == 0):
      return True
      break
    else:
      return False




'''def reto8():
    numeroPedido = int(input('Escribe tu número y te diré si es primo: '))
    for n in range(2, numeroPedido):
        if (numeroPedido % n == 0):
            print('El numero no es primo')
            break
        else:
            print('El numero es primo')'''