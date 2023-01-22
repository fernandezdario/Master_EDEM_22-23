#Reto 13: Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo
import math
def reto13():
    base = int(input('Escribe la base del triángulo: '))
    height = int(input('Escribe la altura del triángulo: '))
    radius = int(input('Escribe el radio del circulo: '))
    def areaTriangle(a: int, b: int):
        return (a * b * 0.5)
    print(f'El area del triángulo es : {areaTriangle(a = base, b = height)}')
    def areaCircle(r: int):
        return (math.pi * r**2)
    print(f'El area del circulo es: {areaCircle(r = radius)}')
reto13()