# Tools for online experiments done with oTree
**Programmer:** Marco Gutierrez

Aquí podrás encontrar un ejemplo sobre cómo debe ser la versión final
del código de un experimento online.

Este incluye:

1. El código en español para un Trust Game
1. Bloqueador de dispositivos móviles
1. Quiz Dinámico de Entendimiento
1. Página Final con Información de Pagos

La estructura que deben tener estos experimentos debe ser la siguiente:

1. Añadir el bloqueador de móviles como la primera aplicación a ejecutar
1. Luego, deben presentarse las instrucciones y el quiz de entendimiento
1. Después se debe ejecutar el codigo con la interaccion de interes sobre el experimento
1. Finalmente, se les muestra la página de pagos

Adicionalmente, cada página del experimento debe incluir lo siguiente

- Instrucciones como botón desplegable al final (no incluirlo en el quiz)
- Botón de contacto con nro y correo del lab (trust_production incluye esos datos)
- Etiqueta del participante debe estar en el extremo superior derecho de cada página (ver trust_production e initial quiz)

El proyecto debe incluir:
- Un room llamado e2laup-room definido en settings
- Un archivo de etiquetas llamado e2laup-room dentro de _rooms

### TODO List (Para quienes usen el repo)
1. Seleccionar una ronda al azar del exp como la ronda a pagar
1. Añadir funcion de pagos que sume lo obtenido en quiz y experimento
1. Mostrar al final de todas las tareas el pago final del experimento (quiz+interacciones)