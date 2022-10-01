'''EJERCICIO
- Por consola el usuario debe acertar un número secreto
- Tiene 3 intentos
- Si acierta en el primer intento: Se suman 5 puntos y el resultado se multiplican por 2
- Si acierta en el segundo intento: Se suman 5 puntos
- Si acierta a la tercera: Se suma 2 puntos
- Si falla todas las veces: Se resta 2 puntos'''


#Esta es la forma de hacerlo únicamente con los intentos, sin sumar los puntos.
'''numeroSecreto = 10
puntos = 2
intentos = 0 #Cuando inicias los intentos partes desde 0, por eso tienen que indicarle que este es el inicio.

while intentos<3:#Aquí lo que le indicamos es que mientras el número de intentos sea menor a 3 haga el bucle de while, de tal forma que nos pedirá que elijamos un número mientras que no lo acertemos.
  numeroElegido = int(input("Elige un número: "))
  if numeroElegido != numeroSecreto:#Aquí le indicamos que si el numero elegido es distinto al secreto (300) que nos diga que el número es erroneo.
    print('Error. El número secreto no es correcto.')
  else: 
    print('El número elegido es el correcto.')
    break#Con el break le decimos a la consola que cierre el bucle cuando nos equivoquemos para que nos permita volver a empezar y elegir el número o que pare el bucle cuando acertemos.
  intentos +=1#Con esto partimos de cero errores, pero cada vez que no sea correcto el número nos sumará un intento más
if intentos == 3:#En este caso cuando ya hayamos sumado los 3 intentos nos dirá que ya no podemos hacerlo más porque se han acabado los intentos.
  print('Has sobrepaso los 3 intentos disponibles.')
'''


#Alternativa 2
numeroSecreto = 10
intentos = 3
puntos = 2
numeroElegido = int(input(f'Debes adivinar el numero secreto, empiezas con {puntos} puntos y {intentos} intentos: '))

while (numeroElegido != numeroSecreto and intentos != 0):
  if (intentos == 1):
    print(f'Has perdido, has fallado las 3 veces, ahora tienes {puntos - 2} puntos.')
    intentos -= 1
  else:
    if (numeroElegido > numeroSecreto):
      intentos -= 1
      numeroElegido = int(input(f'El numero secreto es menor, te quedan {intentos} intentos.'))
    else:
      intentos -= 1
      numeroElegido = int(input(f'El numero secreto es mayor, te quedan {intentos} intentos.'))
if(numeroElegido == numeroSecreto and intentos == 3):
  print(f'Has ganado el numero secreto era {numeroSecreto}, ahora tienes {puntos * 2 + 5} puntos.')
elif (numeroElegido == numeroSecreto and intentos == 2):
  print(f'Has ganado el numero secreto era {numeroSecreto}, ahora tienes {puntos + 5} puntos.')
elif (numeroElegido == numeroSecreto and intentos == 1):
  print(f'Has ganado el numero secreto era {numeroSecreto}, ahora tienes {puntos + 2} puntos.')

