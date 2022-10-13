'''Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS os clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa'''


class Cliente():
    nif: str
    name: str
    surname: str
    telephone: str
    email: str
    preference: bool

    def __init__(self, nif, name, surname, telephone, email, preference):
        self.nif = nif
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email
        self.preference = preference

    clientes = []
    
    def add(self, nif, name, surname, telephone, email, preference):
        self.name = input('Escribe el nombre:')
        self.nif = input('Escribe el DNI:')
        self.surname = input('Escribe el appellido:')
        self.telephone = input('Escribe el telefono:')
        self.email = input('Escribe el email:')
        self.preference = input('Escribe si eres preferente, si es así se pone True y viceversa:')