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
cartera_clientes = []
eleccion = 0
print('Bienvenido a la pantalla de seleccion de la carte de clientes! A continuación, apareceran una serie de comandos que puedes accionar.')
while eleccion != 6:
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
        cliente_nuevo = Clientes(NIF, nombre, apellido, telefono, email, preferente)
        cartera_clientes.append(cliente_nuevo)
    elif eleccion == 2:
        print('Has seleccionado la opción de eliminar un cliente por NIF.')
        NIF = str(input('Escribe el NIF del cliente que quieras eliminar: '))
        for cliente in cartera_clientes:
            if cliente.NIF == NIF:
                cartera_clientes.remove(cliente)
                print('El cliente ha sido eliminado, de manera exitosa!')
            else:
                print('No existe este NIF.')
                break
    elif eleccion == 3:
        print('Has seleccionado la opción de listar un cliente por NIF.')
        NIF = str(input('Escribe el NIF del cliente que quieras encontrar: '))
        for cliente in cartera_clientes:
            if cliente.NIF == NIF:
                print(f'\n\nNIF: {NIF}\nNombre: {cliente.nombre}\nApellidos: {cliente.apellido}\nTelefono: {cliente.telefono}\nEmail:{cliente.email}\nPreferente: {cliente.preferente}')
            else:
                print('Este NIF no existe.')
                break
    elif eleccion == 4:
        print('Has seleccionado la opción de mostrar todos los clientes.')
        for cliente in cartera_clientes:
            print(f'\n\nNIF: {cliente.NIF}\nNombre: {cliente.nombre}\nApellidos: {cliente.apellido}\nTelefono: {cliente.telefono}\nEmail:{cliente.email}\nPreferente: {cliente.preferente}')
    elif eleccion == 5:
        print('Has seleccionado la opción de mostrar todos los clientes preferentes.')
        for cliente in cartera_clientes:
            if cliente.preferente == True:
                print(f'\n\nNIF: {cliente.NIF}\nNombre: {cliente.nombre}\nApellidos: {cliente.apellido}\nTelefono: {cliente.telefono}\nEmail:{cliente.email}\nPreferente: {cliente.preferente}')
    elif eleccion == 6:
        break
    else:
        print('Este programa solo contempla acciones del 1 al 6, por favor vuelva a introducir una acción que se contemple en los parámetros del programa.')
        eleccion = int(input('(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nAcción escogida: '))
