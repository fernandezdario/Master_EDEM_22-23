# Redes recurrentes-NLP

## Preprocesado

- Corregir errores con Regex
- Quitar acentos, signos de puntuación, mayúsculas, hay que dejar el texto lo más uniforme posible
- Eliminar Stop Words: preposiciones, conjunciones, es decir, palabras que no aportan valor al textp

## Bag of Words

- En el procesamiento del lenguaje natural (NLP), Bag of Words (BoW)es una técnica común utilizada para la representación de texto.
- La idea principal detrás de esta técnica es que se puede representar un documento como un conjunto de palabras sin importar la estructura gramatical y el orden en el que aparecen las palabras en el texto.

#### ¿Cómo se utiliza?

El proceso para crear un modelo BoW se puede resumir en los siguientes pasos:

1. Limpieza del texto: Se eliminan los caracteres no deseados y las stop-words.
2. Tokenización: Se divide el texto en palabras o términos individuales.
3. Construcción del vocabulario: Se crea un vocabulario de todas las palabras únicas encontradas en el corpus.
4. Codificación del texto: Se cuenta la frecuencia de cada palabra en cada documento y se crea una matriz donde cada fila representa un documento y cada columna representa una palabra en el vocabulario.

