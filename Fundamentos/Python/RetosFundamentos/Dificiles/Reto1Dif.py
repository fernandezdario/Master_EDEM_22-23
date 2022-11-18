from datetime import date
Un_Verano_Sin_Ti = {
'Nombre' : 'Un verano sin ti',
'Artista' : 'Bad Bunny',
'Año' : '2022',
'Precio' : 15,
'Genero' : 'Reggaeton'
}
Filosofem = {
'Nombre' : 'Filosofem',
'Artista' : 'Burzum',
'Año' : '1996',
'Precio' : 16,
'Genero' : 'Black Metal'
}
Random_Access_Memories = {
'Nombre' : 'Random Access Memories',
'Artista' : 'Daft Punk',
'Año' : '2013',
'Precio' : 15,
'Genero' : 'Electro'
}
Nevermind = {
'Nombre' : 'Nevermind',
'Artista' : 'Nirvana',
'Año' : '1991',
'Precio' : 17,
'Genero' : 'Rock'
}
Back_To_Black = {
'Nombre' : 'Back to Black',
'Artista' : 'Amy Winehouse',
'Año' : '2006',
'Precio' : 18,
'Genero' : 'Pop'
}  
Masters_Of_Puppets = {
'Nombre' : 'Master of Puppets',
'Artista' : 'Metallica',
'Año' : '1986',
'Precio' : 16,
'Genero' : 'Metal'
}
Human = {
'Nombre' : 'Human',
'Artista' : 'Death',
'Año' : '1991',
'Precio' : 16,
'Genero' : 'Death Metal'
}
Appetite_For_Destruction = {
'Nombre' : 'Appetite for Destruction',
'Artista' : 'Guns and Roses',
'Año' : '1987',
'Precio' : 20,
'Genero' : 'Metal'
}
Dawn_FM = {
'Nombre' : 'Dawn FM',
'Artista' : 'The Weeknd',
'Año' : '2022',
'Precio' : 18,
'Genero': 'Electro'
}



input('Bienvenido a la caja registradora, pulsa enter para empezar :)')
print('Estos son los siguientes albumes disponibles para compra: \n1º: Un verano sin ti \n2º: Filosofem \n3º: Random Access Memories \n4º: Nevermind \n5º: Back to Black \n6º: Masters of Puppets \n7º: Human \n8º: Appetite for Destruction \n9º: Dawn FM')
eleccion = int(input('Escoge un numero del 1 al 9 para seleccionar el album que desees: '))

if eleccion == 1:
  print(Un_Verano_Sin_Ti)
  nombre = Un_Verano_Sin_Ti['Nombre'] #ponemos la variable de nombre para que al final cuando queramos imprimir el ticket de la compra que coja el nombre del album
  disco = Un_Verano_Sin_Ti
elif eleccion == 2:
  print(Filosofem)
  print('Este album tiene un descuento del 30%, el precio final es de: 11,2€')
  nombre = Filosofem['Nombre']
  disco = Filosofem
elif eleccion == 3:
  print(Random_Access_Memories)
  print('Este album tiene un descuento del 30%, el precio final es de: 10,5€')
  nombre = Random_Access_Memories['Nombre']
  disco = Random_Access_Memories
elif eleccion == 4:
  print(Nevermind)
  nombre = Nevermind['Nombre']
  disco = Nevermind
elif eleccion == 5:
  print(Back_To_Black)
  nombre = Back_To_Black['Nombre']
  disco = Back_To_Black
elif eleccion == 6:
  print(Masters_Of_Puppets)
  nombre = Masters_Of_Puppets['Nombre']
  disco = Masters_Of_Puppets
elif eleccion == 7:
  print(Human)
  nombre = Human['Nombre']
  disco = Human
elif eleccion == 8:
  print(Appetite_For_Destruction)
  nombre = Appetite_For_Destruction['Nombre']
  disco = Appetite_For_Destruction
elif eleccion == 9:
  print(Dawn_FM)
  print('Este album tiene un descuento del 30%, el precio final es de: 12,6€')
  nombre = Dawn_FM['Nombre']
  disco = Dawn_FM

numero = int(input(f'Finalmente has escogido el album {nombre}, pulse la tecla 0 para terminar con la compra.'))
if numero == 0:
  print(f'Total a pagar: {round(disco[("Precio")],2)}€')
  print('Muchas gracias por su compra! :)')
  if disco == Filosofem:
    print(f'En esta compra se ha ahorrado: ' + str(0.3*16) + '€')
  elif disco == Random_Access_Memories:
    print(f'En esta compra se ha ahorrado: ' + str(0.3*15) + '€')
  elif disco == Dawn_FM:
    print(f'En esta compra se ha ahorrado: ' + str(0.3*18) + '€')
  dia = date.today()
  print(f'Fecha de compra: {dia}')