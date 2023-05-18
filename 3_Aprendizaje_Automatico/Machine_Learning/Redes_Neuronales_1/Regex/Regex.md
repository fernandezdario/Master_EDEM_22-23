# Expresiones regulares
 Estos son los ejercicios de la clase del jueves 11/05/2023
- Para un NIF: [0-9]{8}[A-Z]{1}
- Para una fecha con formato dd/mm/aa: [0-9]{2}\/[0-9]{2}\/[0-9]{2}
- Para un telefono fijao, sabiendo que empieza por 9: 9[0-9]{8}

- Encontrar numeros del 1980 al 1999: \b19[89][0-9]\b
- Encontrar numeros del 1981 al 1999: \b19[89][1-9]|19[89][0-9]\b
- Encontrar fechas en el formato dd/mm/aa y que no acepte valores imposibles: \b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/([0-9]{2})\b

