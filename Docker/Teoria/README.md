Hablemos un poco de Virtualización y sus entornos
------
------

Virtualización
------
Una maquina virtual se trata de la creación de maquinas de hacer de una sola a muchas maquinas con menores recursos, pero adaptados a los requisitos que se necesitan.

La creación de MV da como resultado un sistema mucho más seguro y eficiente que tener máquinas propias, ya que, si tratan de hackear una máquina de una empresa con muchas aplicaciones, solo pueden hackear la aplicación a la que han accedido, no tienen la capacidad de entrar al resto.

Las máquinas virtuales te permiten tener diferentes sistemas operativos en las maquinas virtuales. Por ejemplo, tienes un Windows y necesitan una aplicación de Mac, puedes crear una maquina virtual con Mac y acceder a dicha aplicación.

En cuanto a las maquinas virtuales tenemos que saber que las empresas nos ofrecen maquinas virtuales por default. Sin embargo, podemos tener maquinas virtuales que no tengan nada y creemos nosotros las imágenes que necesitamos.

### Tipos de Virtualización

1. Virtualización de servidores
    - Permite la ejecución de múltiples sistemas operativos en un único servidor físico
    - Reducción de los costes operativos
    - Mayor disponibilidad del servidor
2. Virtualización de la red
    - Reproducción de una red física
    - Permite que las aplicaciones se ejecuten en una red virtual
3. Virtualización del escritorio
    - Permite a las organizaciones de TI responder más rápidamente a las necesidades cambiantes del lugar de trabajo y a las nuevas oportunidades
4. Virtualización del almacenamiento
    - Visión lógica de los recursos físicos de almacenamiento

A modo de curiosidad, es interesante conocer a los proveedores más importante de virtualizaci´pn en la nube:

- Google Compute Engine (GCE)
- Amazon Elastic Compute Cloud (EC2)
- Azure Virtual Machines

Hypervisor
------

Un hipervisor es un software, firmware o hardware informático que crea y ejecuta máquinas virtuales.

Es un proceso que separa el sistema operativo y las aplicaciones del hardware físico subyacente.

Aunque las máquinas virtuales pueden ejecutarse en el mismo hardware físico, siguen estando lógicamente separadas unas de otras entre sí. Esto significa que si una VM experimenta un error, un fallo o un ataque de malware, no se extiende a otras máquinas virtuales de la misma máquina.

Integración Continua (CI) y Desarrollo Continuo (CD)
------

### Desarrollo Continuo (CD)

En cuanto al Desarrollo Continuo podemos encontrar cuatro entornos:

•	Entorno de desarrollo: Se trata de un desarrollo local en mi ordenador.

•	Entorno de integración: Es cuando todo aquello que he creado en mi entorno de creación local para que el resto puedan trabajar en lo que hemos creado nosotros previamente.

•	Entorno User Acceptance Testing: En este caso se evalúa lo trabajado previamente por aquellas personas que saben lo que los usuarios quieren y si todo funciona de tal forma que los usuarios tienen lo que quieren. Es decir, se evalúa si se cumplen los requisitos especificados.

•	Entorno de seguridad

•	Entorno de producción: Es el entorno final, en el cual el cliente se moverá.

Actualmente los ciclos de desarrollo de software son muy cortos y se debe ir informando al cliente de forma constante sobre el desarrollo del software, por tanto, es interesante aplicar otros métodos como el Agile Methodology, de esta manera hay continuo flujo de información entre el cliente y el desarrollador, de tal manera que existe un feedback constante entre el desarrollador y el cliente ante un mercado tan volátil como el actual.

### Integración Continua (CI)
La integración continua es una filosofía de codificación y un conjunto de prácticas que que impulsan a los equipos de desarrollo a implementar pequeños cambios y comprobar el código a los repositorios de control de versiones con frecuencia.

- La idea es establecer una manera consistente y automatizada de construir, empaquetar y probar las aplicaciones.
- Los cambios del desarrollador se validan creando una compilación y ejecutando prueba automatizada contra la compilación.
