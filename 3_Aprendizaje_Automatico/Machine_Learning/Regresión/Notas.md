# Regresión

## Regresión Lineal

La regresión es una técnica de aprendizaje superevisado para predecir a partir de un histórico.

- Predicción de valores
- Relacíon entre variables al modelo
- Importancia de las características del modelo

## Problemas al aumentar la dimensión

- Sampling Bias: las muestras de datos no son representativas

## ¿Cuántas características debe tener un modelo?



## Selección de varibles
Seleccionas un Subconjunto óptimo de caracteristicas relevantes que nos permitan construir un modelo útil

## Extracción de variables
Creas un Nuevo Cobnjunto de características relevantes para crear un modelo útil

## Dimensionality Reduction

¿porque se hace esta reduccion de la dimensionalidad?

- Maldición de la Dimensión
- Garbage in, garbage out
- Navaja de Ockham: Entre dos teorías en igualdad de condicones que tienen las mismas consecuencias, la explicación más sencilla suele ser la más coherente
- Modelos más sencillos de entrenar
- Menor tiempo computacional

### Feature Selection o Feature Extraction

Falta explicación

## Métodos de Filtros

- La slección de variables es independiente de los modelos de ML
- Clasificación de las varaibles en función de la correlacion que tienen con el output
- Se utilizan criterios univariados

Todas caract. > Seleccionamos mejor subconjunto > Algoritmo Learning > Performance

### ¿Que método existen?

- Varianza: Elimina variables que son constantes o casi constantes
- Chi-cuadrado: Es un test de independencia estadística que determina la dependencia de 2 variables categóricas
- Correlación de Pearson: Medimos dependencia lineal entre 2 variables

## Ventajas y Desventajas

### Ventajas
- Reducción de tiempo de procesamiento y almacenamiento
- Mejora la interpretación
- Reducción del Overfitting

### Desventajas
- Analizan las variables de forma individual
- No detectan la correlación grupal

# t-SNE

- Se trata de una técnica para visualizar datos de alta dimensión (más de 10 dimensiones) con Extraction Features.
- Las observaciones que son similares estarán más cercanas entre si y pueden aruparse.
- No funciona con variables categóricas.
- Captura relaciones No lineales entre variables.


