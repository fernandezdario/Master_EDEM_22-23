#Reto 16: Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola

from datetime import date

fecha_inicial = date(2021,8,10)
fecha_final = date(2019,8,10)

resultado = (fecha_inicial - fecha_final)

print(resultado.days)