#Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
#Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego terminar.
def reto5():
  print('Bienvenido al sistema!')
  user_ = 'Dario'
  user = input('Escribe tu usuario: ')
  contraseña = 'admin'
  password:str = input('Introduce una contraseña: ')
  while password != contraseña:
    print('La contraseña no es correcta.')
    password = input('Inténtalo otra vez:')
  print('Bienvenido al programa señor ADMIN!')