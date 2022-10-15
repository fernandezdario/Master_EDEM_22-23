'''Reto 9
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no'''
def reto9():
    def leap_year(year: int):
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)#la formula para saber si es año bisiesto o no es que el año sea divisible entre 400 o 4 y que no sea solamente divisible entre 100.

    while not leap_year(int(input('introduce año: '))):#en este caso, mientras que el año introducido no cumpla con las condiciones anteriores(que sea bisiesto), nos volverá a pedir que introduzcamos un numero
        print('ese año no es bisiesto')
    print('Has acertado, el año es bisiesto')#lo ponemos fuera del while porque no está dentro del bucle de los años no bisiestos, esto se imprimirá cuando el año sea bisiesto.