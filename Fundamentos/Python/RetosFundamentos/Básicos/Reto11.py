'''Reto 11
Escribe un programa que pida al usuario los siguientes datos por consola:
Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula"'''

title = input('Escribe el título de la película: ')
director = input('Escribe el nombre del director: ')
year = int(input('En que año se estrenó está pelicula?: '))
country = input('Escribe el país donde se grabó esta película:')

pelicula = {
    'Título de la película': title,
    'Director': director,
    'Año de estreno': year,
    'País': country
}

print(pelicula)