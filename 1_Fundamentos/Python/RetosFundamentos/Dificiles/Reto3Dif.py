contribuyentes = []
ingresos = int(input('Indique sus ingresos mensuales: '))

edad_contribuyente = int(input('Indique su edad: '))

'''def deudas(ingresos, edad_contribuyente):
    if edad_contribuyente <= 16 or edad_contribuyente >= 70:
        print('No se debe pagar nada.')
    else:
        if ingresos <= 800:
            a = (ingresos * 0.1 * 12)
            print(f' Debes pagar una deuda acumulada de {a}')
        elif 800 >= ingresos <= 2000:
            b =(ingresos * 0.3 * 12)
            print(f' Debes pagar una deuda acumulada de {b}')
        elif ingresos >= 2000:
            c = (ingresos * 0.5 * 12)
            print(f' Debes pagar una deuda acumulada de {c}')'''


if edad_contribuyente <= 16 or edad_contribuyente >= 70:
        print('No se debe pagar nada.')
else:
    if ingresos <= 800:
        a = (ingresos * 0.1 * 12)
        print(f'Debes pagar una deuda anual acumulada de {a} y una deuda mensual de {a/12}')
    elif 800 >= ingresos <= 2000:
        b =(ingresos * 0.3 * 12)
        print(f'Debes pagar una deuda anual acumulada de {b} y una deuda mensual de {b/12}')
    elif ingresos >= 2000:
        c = (ingresos * 0.5 * 12)
        print(f'Debes pagar una deuda anual acumulada de {c} y una deuda mensual de {c/12}')