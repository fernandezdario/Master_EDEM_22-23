# KAFKA

## Introducción

**Definición:**

> Apache Kafka es una plataforma de streaming distribuido.
> Apache Kafka es una cola de mensajes pub/sub en tiempo real, tolerante a fallos y altamente escalable, diseñada como un registro de transacciones distribuido.

**Componentes:**

*1. Producers:* Permite a una aplicación publicar un flujo de registros en uno o más temas de Kafka.
*2. Consumers:* Permite que una aplicación se suscriba a uno o varios temas y procese el flujo de registros producidos en ellos
*3. Connectors:* Permite crear y ejecutar productores o consumidores reutilizables que conectan temas de Kafka a aplicaciones o sistemas de datos existentes.
*4. Streams:* Permite que una aplicación actúe como un procesador de flujos, consumiendo un flujo de entrada de uno o más temas y produciendo un flujo de salida hacia uno o más temas de salida, transformando efectivamente los flujos de entrada en flujos de salida.

**Sistemas de Mensajería:**

- *Point to Point Messaging System*
En un sistema punto a punto, los mensajes se almacenan en una cola. Uno o varios consumidores pueden consumir los mensajes de la cola, pero un mensaje concreto sólo puede ser consumido por un consumidor como máximo. 
Una vez que un consumidor lee un mensaje de la cola, éste desaparece de la misma.

![Point to Point Messaging System](2_Tratamiento_dato/Kafka/../../Imagenes/ptp.png)

- *Publish-Subscribe Messaging System:*
En el sistema de publicación-suscripción, los mensajes se almacenan en un tema. A diferencia del sistema punto a punto, los consumidores pueden suscribirse a uno o varios temas y consumir todos los mensajes de ese tema. En el sistema Publish-Subscribe, los productores de mensajes se denominan editores y los consumidores de mensajes, suscriptores. 

![Publish-Subscribe Messaging System](2_Tratamiento_dato/Kafka/../../Imagenes/ps.png)
