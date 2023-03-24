# Modelos Lineales

## Clasificación vs Regresión

En el caso de la regresión podremos ver como el target es numérico, es decir el target será una variable numérica, mientras que en el caso de la clasificación podremos ver como el target cambia hacia las varaibles categóricas, hay que tener cuidado con este tipo de estrategia a seguir con cada uno de los dos tipos.

### Regresión

- MAE: Este método es el mejor que puedes usar en el caso de maximizar el revenue.
- MAPE: Este tipo de método es el mismo que se emplea con el MAE, pero este lo hace en porcentaje.

### Clasificación

- Accuracy: Es la peor métrica que puedes usar, ya que no se mira la precisión por clase, sino que es algo global y si tienes un problema desbalanceado tendrás bastante problemas. En el caso de que se realice este indicador por clases no se generarán tantos problemas.
- Sesibilidad: Es la capacidad de un modelo para detectar las clases positivas. Es decir, es la capacidad de un modelo para detectar los casos positivos. Por ejemplo, si tenemos un modelo que detecta si una persona tiene cáncer o no, la sensibilidad es la capacidad de este modelo para detectar a las personas que tienen cáncer.
- Especificidad: Es la capacidad de un modelo para detectar las clases negativas. Es decir, es la capacidad de un modelo para detectar a las personas que no tienen cáncer. Por ejemplo, si tenemos un modelo que detecta si una persona tiene cáncer o no, la especificidad es la capacidad de este modelo para detectar a las personas que no tienen cáncer.
- Precisión: Es la capacidad de un modelo para PREDECIR CORRECTAMENTE las clases positivas. Es decir, es la capacidad de un modelo para predecir correctamente a las personas que tienen cáncer. Por ejemplo, si tenemos un modelo que detecta si una persona tiene cáncer o no, la precisión es la capacidad de este modelo para predecir correctamente a las personas que tienen cáncer.
- F1 Score: Es la media armónica entre la sensibilidad y la precisión. Es decir, es la media armónica entre la capacidad de un modelo para detectar las clases positivas y la capacidad de un modelo para predecir correctamente las clases positivas. Por ejemplo, si tenemos un modelo que detecta si una persona tiene cáncer o no, el F1 Score es la media armónica entre la capacidad de este modelo para detectar a las personas que tienen cáncer y la capacidad de este modelo para predecir correctamente a las personas que tienen cáncer.

# Modelos no lineales

- SVM: Es un modelo que se basa en la distancia entre los puntos, es decir, se basa en la distancia entre los puntos para poder realizar la clasificación. Este modelo es muy bueno para realizar clasificaciones no lineales.

Los modelos que vamos a ver ahora sirven tanto para clasificación como para regresión.

