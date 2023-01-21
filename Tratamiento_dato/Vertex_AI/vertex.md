# Vertex AI - GCP

AutoML es una herramienta de Vertex, la cual es bastante eficiente ya que te permite saber cuales son las mejores columnas para hacer el análisis y cuáles le resultan inútiles al modelo, mientras nosotros lo entrenamos.

**Machine Learning Workflow:**

- Data Preparation
- Model Training
- Model evaluation and iteration
- Model deployment and serving
- Model monitoring

**AutoML:**

- Esta herramienta nos permite entrenar un amplio rango de modelos de forma que no nos preocupemos por los detalles, ya que esta herramienta entrena una gran cantidad de modelos, hasta que finalemente te entrega el modelo ganador.
- Estos modelos se pueden limitar a una cantidad de tiempo para ahorrarnos costes a la hora del entrenamiento.
- Esta herramienta es muy poco configurable, ya que hay muy pocos parámetros.

**PlatformAI:**

Se trata de una libreria para entrenar modelos de AI utilizando nuestro propio código. Además, esta herramienta te permite acceder al resto de ventajas que proporciona Vertex AI, aunque es un poco más complicado de usar que el AutoML.

**Datasets:**

- Datos Tabulados (CSV, Excel)
- Imágenes
- Video
- Texto

*Datos Tabulados:*

- La primera linea debe ser el header.
- No pueden pesar los CSV más de 10GB.
- El delimitador debe ser la coma
- Al menos 1.000 filas para poder entrenar el modelo correctamente.
- El CSV se sube con la variable a predecir incluida.

Para entrenar el modelo de forma correcta es dividir los datos para que el modelo no se aprenda los datos y de esa forma podremos saber si el modelo está entrenado correctamente o no. Por tanto, se puede repartir los datos entre entrnamiento, validación y test.

#### Métricas Modelo

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

**Fórmulas:** (Rellenar fórmulas que faltan)

- *Accuracy* = (TP + TN)/(TP + TN + FP + FN) -> Cuantos he acertado de cuantos hay
- *Precision* = TP/(TP + FP) -> Te indica cuantas has acertado de una clase en concreto
- *Recall* = TP/(TP + FN) -> Ente 0 y 1, siendo 1 lo mejor
- *F1 Score*: Es la media armónica de la Precision y el Recall
- *ROC Curve*: Cuanto más se situe a la izquierda superior más perfecto es nuestro modelo.


En una matriz de 2 x 2, el cuadrante de la derecha arriba y la izquierda abajo nos muestra los fallos que ha habido de todas las muestras que se le dan para que lo evalúe, a menor valor en esos cuadrantes mayor sea la accuracy del modelo.

#### Información Modelo

Vertex te permite saber que columnas son las que más han ayudado a la IA a crear el modelo, por tanto, este herramienta es capaz de ayudarte a identificar y a aislar aquellas variables con mayor relevancia para el modelo que se entrene.

