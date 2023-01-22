import math

radius = int(input('Escribe el radio del circulo: '))
height = int(input('Escribe la altura para el volumen del cilindro:'))
def areaCirculo(r: int):
    return (math.pi * radius**2)
def volCilindro(r: float, h: float):
    return (areaCirculo(r) * h)
print(f'El volumen del cilindro es: {volCilindro(r = radius, h = height)}')
