'''Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS los clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa'''

from Clientes import Clientes
cliente1 = Clientes('45464148J', 'Joaquin', 'Reyes Gomez', '694564123','joarego@gmail.com', preferente = False)
cliente2 = Clientes('45464348D', 'Fernando', 'Sebastian Lopez', '642789453','nandose@gmail.com', preferente = True)
cliente3 = Clientes('35428342D', 'Paco', 'Beltran Torres', '621248795','pabeto@gmail.com', preferente = True)
cliente4 = Clientes('66666666F', 'Pablo', 'Gonzalez Martinez', '654987321', 'pagonza@edem.es', preferente = False)
cartera_clientes = [cliente1, cliente2, cliente3, cliente4]
eleccion = 0
print('Bienvenido a la pantalla de seleccion de la carte de clientes!')
while eleccion != 6:
    print('Bienvenido al sistema! A continuación, apareceran una serie de comandos que puedes accionar.')
    eleccion = int(input('(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nAcción escogida: '))
    if eleccion == 1:
        # creamos los valores del diccionario, de forma interactiva, mediante consola
        NIF = str(input('Escribe aquí tu NIF: '))
        nombre = str(input('Escribe aquí tu nombre: '))
        apellido = str(input('Escribe aquí tus apellidos: '))
        telefono = str(input('Escribe aquí tu teléfono: '))
        email = str(input('Escribe aquí tu email: '))
        preferente = bool(input('¿Tiene un contrato preferente? En caso de que así sea escriba True, en caso contrario False: '))
        #aquí le damos a los valores creados previamente unas claves para que se puedan alamacenar en el diccionario
        cliente = Clientes(NIF, nombre, apellido, telefono, email, preferente)
        cartera_clientes.append(cliente)
    elif eleccion == 2:

        print(f"\nHas seleccionado ({eleccion}): Has seleccionado eliminar un cliente por NIF")
  
        NIF = str(input("Introduzca el NIF: "))

        for n in Clientes:
            if n.NIF == NIF:
                Clientes.remove(n)

# Si introducimos 3: Mostramos un cliente de la carteta según el NIF
    elif eleccion == 3:

        print(f"\nHas seleccionado ({eleccion}): Has seleccionado mostrar un cliente por NIF")

        NIF = str(input("Introduzca el NIF: "))
    for n in Clientes:
      if n.NIF == NIF:
         print(f'\n\nNIF: {n.NIF}\nNombre: {n.nombre}\nApellidos: {n.apellidos}\nTelefono: {n.telefono}\nEmail:{n.email}\nPreferente: {n.preferente} ')