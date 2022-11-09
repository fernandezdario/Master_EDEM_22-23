'''Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS los clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa'''
import csv
clientes = {}

def cartera_cientes():
    print('Bienvenido al sistema! A continuación, apareceran una serie de comandos que puedes accionar.')
    eleccion = int(input('(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nAcción escogida: '))

    if eleccion == 1:
        # creamos los valores del diccionario, de forma interactiva, mediante consola
        nif = str(input('Escribe aquí tu NIF: '))
        nombre = str(input('Escribe aquí tu nombre: '))
        apellidos = str(input('Escribe aquí tus apellidos: '))
        telefono = str(input('Escribe aquí tu teléfono: '))
        email = str(input('Escribe aquí tu email: '))
        preferente = bool(input('¿Tiene un contrato preferente? En caso de que así sea escriba True, en caso contrario False: '))
        #aquí le damos a los valores creados previamente unas claves para que se puedan alamacenar en el diccionario
        cliente = {'NIF': nif, 'Nombre': nombre, 'Apellidos': apellidos, 'Telefono': telefono, 'Email': email, 'Preferente': preferente}
        clientes[nif] = cliente
        #el programa guarda el diccionario en un csv y almacena los datos en formato clave, valor. En este caso la clave será el nif, mientras que el valor será el resto del diccionario.
        with open('C:\\Users\\dario\\OneDrive\\Documentos\\GitHub\\M-ster-EDEM-22-23\\Fundamentos\\Python\\RetosFundamentos\\Dificiles\\clientes.csv', 'a') as g:  
            a = csv.writer(g)
            for k, v in clientes.items():
                a.writerow([k, v])
    if eleccion == 2:
        print('Has seleccionado la opción de eliminar un cliente por NIF.')
        nif = str(input('Escribe el NIF del cliente que quieras eliminar: '))
        if nif in clientes:
            del cliente
            with open('C:\\Users\\dario\\OneDrive\\Documentos\\GitHub\\M-ster-EDEM-22-23\\Fundamentos\\Python\\RetosFundamentos\\Dificiles\\clientes.csv', 'w') as g:  
                writer = csv.writer(g)
                for k, v in clientes.items():
                    writer.writerow([k, v])
        else:
            print('No existe este NIF.')
    if eleccion == 3:
        nif = str(input('Escribe el NIF del cliente que quieras encontrar: '))
        if nif in clientes:
            print(cliente)
        else:
            print('Este NIF no existe.')
    if eleccion == 4:
        print(clientes)
    if eleccion == 5:
        'sadfsdfsfd'
    if eleccion == 6:
        'sadfsdfsfd'
    else:
        print('Solamente existen comandos del 1 al 6, por favor elija un número comprendido en ese rango.')
        eleccion = int(input('(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nAcción escogida: '))
cartera_cientes()