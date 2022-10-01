'''#Alternativa 1
numeroSolicitado = int(input('Escribe el año aquí para saber si es bisiesto: '))
def anioBisiesto(anio):
  if anio % 4 == 0 and anio % 400 == 0:
    return True
  elif anio % 100 == 0 and anio % 400 == 0:
    return True
  elif anio % 400 == 0:
    return True
  elif anio % 4 == 0: 
    return True
  elif anio % 100 == 0:
    return False
  elif anio % 4 != 0:
    return False

while (anioBisiesto(numeroSolicitado) is False):
  numeroSolicitado = int(input('Has fallado, introduce otro año: '))
  anioBisiesto(numeroSolicitado)
  
print(f'Has ganado, el año {numeroSolicitado} es bisiesto')
'''

'''#Alternativa 2
numeroSolicitado = int(input('Escribe el año aquí para saber si es bisiesto: '))
def anioBisiesto(anio) -> bool:
    if (anio % 100 == 0 and anio % 400 == 0) or anio % 4 == 0 and anio % 100 != 0:
        return True
    else: 
        return False
while (anioBisiesto(numeroSolicitado) is False):
  numeroSolicitado = int(input('Has fallado, introduce otro año: '))
  anioBisiesto(numeroSolicitado)
print(f'Has ganado, el año {numeroSolicitado} es bisiesto')'''


'''numeroSolicitado = int(input('Escribe el año aquí para saber si es bisiesto: '))
def anioBisiesto(anio) -> bool:
    if anio % 400 == 0 or anio % 4 == 0 and anio % 100 != 0:
        return True
    else: 
        return False
while (anioBisiesto(numeroSolicitado) is False):
  numeroSolicitado = int(input('Has fallado, introduce otro año: '))
print(f'Has ganado, el año {numeroSolicitado} es bisiesto')
'''

# not seguido de la función es lo mismo que poner de tras de la función == None o is False

'''#Mejor alternativa
def leap_year(year: int):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

while not leap_year(int(input('introduce año: '))):
    print('ese año no es bisiesto')
# print('has acertado')'''

import calendar #el calendario solo se puede utilizar de aqui para abajo

print(f'El año 2020 es bisiesto? {calendar.isleap(2020)}')