''' PASO POR REFERENCIA
Paso de parámetros por Referencia Los valores simples se pasan, por defecto, por valorLos valores complejos se pasan, por defecto, por referencia ''' 

# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen 
def doblar_valores(numeros):    
  for i,n in enumerate(numeros):        
    numeros[i] *= 2