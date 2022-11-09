'''Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS os clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa'''

import csv
def cartera_cientes():
    cliente = {}

    print('Bienvenido al sistema! A continuación, apareceran una serie de comandos que puedes accionar.')
    eleccion = int(input('(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nAcción escogida: '))

    if eleccion == 1:
        nif = str(input('Escribe aquí tu NIF: '))
        nombre = str(input('Escribe aquí tu nombre: '))
        apellidos = str(input('Escribe aquí tus apellidos: '))
        telefono = str(input('Escribe aquí tu teléfono: '))
        email = str(input('Escribe aquí tu email: '))
        preferente = bool(input('¿Tiene un contrato preferente? En caso de que así sea escriba True, en caso contrario False: '))
        cliente = {'NIF': nif, 'Nombre': nombre, 'Apellidos': apellidos, 'Teléfono': telefono, 'Email': email, 'Preferente': preferente}
        with open('clientes.csv', 'a') as g:  
            a = csv.writer(g)
            for k, v in cliente.items():
                a.writerow([k, v])
    elif eleccion == 2:
        'sadfsdfsfd'
    elif eleccion == 3:
        'sadfsdfsfd'
    elif eleccion == 4:
        'sadfsdfsfd'
    elif eleccion == 5:
        'sadfsdfsfd'
    elif eleccion == 6:
        'sadfsdfsfd'
    else:
        print('Solamente existen comandos del 1 al 6, por favor elija un número comprendido en ese rango.')
        eleccion = int(input('(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nAcción escogida: '))
cartera_cientes()