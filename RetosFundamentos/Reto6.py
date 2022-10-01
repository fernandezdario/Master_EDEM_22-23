#Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
def reto6():
  age = int(input('Escribe tu edad:'))
  if age < 18 :
    print('Eres menor de edad.')
  else:
    print('Eres mayor de edad.')