## NoSQL

### *Introducción*

Las bases de datos NoSQL están diseñadas específicamente para modelos de datos específicos y tienen esquemas flexibles para crear aplicaciones modernas. Las bases de datos NoSQL son ampliamente reconocidas porque son fáciles de desarrollar, por su funcionalidad y el rendimiento a escala.

Las bases de datos NoSQL utilizan una variedad de modelos de datos para acceder y administrar datos. Estos tipos de bases de datos están optimizados específicamente para aplicaciones que requieren grandes volúmenes de datos, baja latencia y modelos de datos flexibles, lo que se logra mediante la flexibilización de algunas de las restricciones de coherencia de datos en otras bases de datos.

### *Almacenamiento de Datos*

La importancia de la arquitectura Big Data tiene al fin y al cabo un gran impacto en diferentes aspectos, tales como:

1. Ingesta
2. Volumen
3. Accesibilidad

Además, podemos encontrar que con las bases de datos no relacionales podemos almacenar diferentes tipos de datos:

- Archivos
- Clave-Valor
- Documentos
- Gráficos
- En memoria
- Indexados

## Archivos

Descripción:

> El almacenamiento de archivos es un sistema distribuido, tolerante a fallos y normalmente compatible con POSIX. Este escompatible con POSIX. Se comporta de forma similar a un sistema de archivos normal y puede almacenar grandes conjuntos de datos, que se dividen en bloques y se replican. 

**Apectos clave:**

- Forma simple y barata de almacenamiento
- Lectura secuencial
- Múltiples formas de almacenamiento
   - Texto o Binario
   - Estrucurado (AVRO) o desestructurado (Imágenes)
   - Orientado a columnas

*Tecnologías:*
![Formatos de almacenamiento](file_storage.png)

## Clave - Valor

Descripción:

> Key-Value Store (o bases de datos orientadas a columnas) es un paradigma de almacenamiento de datos diseñado para almacenar, recuperar y gestionar matrices asociativas, una estructura de datos hoy más conocida como diccionario o tabla hash.

*Tecnologías:*


**Apectos clave:**

- Adecuado para
   - Patrones de acceso muy bien definidos
   - Acceso aleatorio de lectura o escritura
- Se adapta muy bien
- Columnas dinámicas
- Esquema en lectura

## Almacen de documentos

Descripción:

> Un Almacén de Documentos (o base de datos orientada a documentos), o, es un programa informático diseñado para almacenar, recuperar y gestionar información orientada a documentos, también conocida como datos semiestructurados (por ejemplo, JSON o XML).

**Apectos clave:**

- Lenguaje de consulta propio
- Facilidad para almacenar y recuperar documentos
- API REST (para almacenes JSON)

*Tecnologías:*

## Gráficos

Descripción: 

> Una base de datos gráfica es una base de datos que utiliza estructuras gráficas para consultas semánticas con nodos, aristas y propiedades para representar y almacenar datos.

**Apectos clave:**

- Bueno para representar relaciones (redes)
   - Lenguaje de consulta propio
   - Rendimiento
   - Presentación
- No es escalable 

*Tecnologías:*

## Base de Datos en memoria

Descripción:

> Una base de datos en memoria (IMDB, también sistema de base de datos en memoria principal o MMDB o base de datos residente en memoria) es un sistema de gestión de bases de datos que se basa principalmente en la memoria principal para el almacenamiento de datos informáticos. Se contrapone a los sistemas de gestión de bases de datos que utilizan un mecanismo de almacenamiento en disco.

**Apectos clave:**

- Gran rendimiento
- Difícil de gestionar
  - Estado de los datos
  - Distribución (escalabilidad)
- Adecuado como
  - Caché
  - Almacén de datos para aplicaciones de streaming

*Tecnologías:*

## Datos Indexados

Descripción:

> Una base de datos indexada puede considerarse un subtipo de almacén de documentos, que proporciona un motor de búsqueda de texto completo distribuido y multiusuario con una interfaz web HTTP y documentos JSON sin esquema.

**Apectos clave:**

- Comparte muchas características de los almacenes de documentos (QL propio, almacenamiento de documentos, API REST)
- Funciones de búsqueda de texto como
  - Faceting
  - Búsqueda de texto libre
  - Sinónimos
  - Autocompletar

*Tecnologías:*

## Teorema CAP

![CAP Theorem](cap_teorema.png)

