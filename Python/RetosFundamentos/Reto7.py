#Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
def reto7():
  contraseña_usuario = 'password de prueba'
  pswd:str = input('Escriba su contraseña aquí:')
  if contraseña_usuario.upper()==pswd.upper():
    print('El texto introducido coincide.')
  else:
    print('El texto intrducido es diferente.')