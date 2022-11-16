'''Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS los clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa'''


class Clientes():
    def __init__(self, NIF:str, nombre:str, apellido:str, telefono:str, email:str, preferente:bool):
        self.NIF = NIF
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.preferente = preferente
eleccion = 0
cartera_clientes = []
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
    if eleccion == 2:
        nif = input('Escribe aquí el NIF del cliente que quieras borrar: ')
        for n in cartera_clientes:
            if nif == NIF:
                cartera_clientes.remove(n)
        