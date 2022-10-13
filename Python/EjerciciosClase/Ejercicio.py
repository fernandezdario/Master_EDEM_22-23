'''Ejercicio: 
Hacer aplicacion de consola, pidiendo:
nombre
email
contrseña
edad
Y después crear un diccionario usuario con los datos introducidos en consola'''


nombre = input('Escribe tu name: ')
email = input('Ahora escribe aquí tu correo: ')
contraseña = input('¿Cuál es la password asignada?')
edad = int(input('Por último, ¿cuántos años tienes?: '))

Diccionario_Usuario = {
  "nombre": {nombre},
  "email": {email},
  "contraseña": {contraseña},
  "edad": {edad},
}

print(f"Hola: {nombre}. Tienes {edad} años. Tu email es {email}, con la contraseña {contraseña}")


