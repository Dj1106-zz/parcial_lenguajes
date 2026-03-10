Informe – Parcial de Lenguajes de Programación
Introducción

En este trabajo se realizaron varios ejercicios relacionados con conceptos importantes de los lenguajes de programación, como el uso de expresiones regulares, el reconocimiento de patrones, el análisis léxico y sintáctico, y la comparación entre diferentes tipos de lenguajes. Para resolver los ejercicios se utilizaron distintos lenguajes y herramientas como Python, C, Flex y Bison. Cada uno de los puntos permitió entender mejor cómo funcionan los lenguajes de programación y algunas de las herramientas que se utilizan en la construcción de compiladores.

Punto 1 – Validación de movimientos de ajedrez con expresiones regulares

En este punto se desarrolló un programa que permite validar ciertos movimientos de ajedrez utilizando expresiones regulares. La idea era reconocer patrones específicos dentro de una cadena de texto y verificar si corresponden a movimientos válidos.

Para esto se utilizó Python y su módulo de expresiones regulares. El programa recibe un movimiento ingresado por el usuario y revisa si coincide con el patrón definido, el cual incluye ejemplos como p->k4, kbp, X y qn. Si la entrada cumple con el formato esperado, el programa indica que el movimiento es aceptado; de lo contrario, se considera inválido.

Este ejercicio permitió ver cómo las expresiones regulares pueden utilizarse para identificar patrones dentro de un lenguaje y validar la estructura de ciertas entradas.

Punto 2 – Reconocimiento de identificadores

En este ejercicio se implementó un programa que permite validar identificadores siguiendo la expresión regular:

[A-Za-z][A-Za-z0-9]*

Esta regla indica que un identificador debe comenzar con una letra y luego puede contener letras o números. Para resolver el ejercicio también se utilizó Python.

El programa solicita al usuario que ingrese un identificador y verifica si cumple con las reglas definidas. Si el identificador comienza con una letra y el resto de los caracteres son válidos, el programa lo acepta; en caso contrario, lo rechaza.

Este tipo de validación es muy común en los compiladores, ya que los identificadores son los nombres que se utilizan para variables, funciones y otros elementos dentro de un programa.

Punto 3 – Cálculo de raíz cuadrada usando Flex y Bison

En el tercer punto se utilizó Flex y Bison para crear un pequeño programa capaz de calcular la raíz cuadrada de un número.

Flex se utilizó para realizar el análisis léxico, es decir, para reconocer los números que el usuario ingresa por teclado. Por otro lado, Bison se encargó del análisis sintáctico y de ejecutar las acciones necesarias cuando se reconoce una entrada válida.

Para calcular la raíz cuadrada se utilizó el método de Newton-Raphson, que es un método numérico que permite aproximar el valor de una raíz mediante un proceso iterativo. Una vez que el programa reconoce el número ingresado, se aplica este método y se muestra el resultado en pantalla.

Este ejercicio permitió entender mejor cómo trabajan juntos los analizadores léxicos y sintácticos dentro del proceso de construcción de un compilador.

Punto 4 – Comparación de rendimiento entre C y Python

En el  ejercicio se realizó una comparación entre un lenguaje compilado (C) y un lenguaje interpretado (Python). Para esto se implementó el algoritmo recursivo de Fibonacci en ambos lenguajes.

El objetivo fue medir el tiempo que tarda cada programa en ejecutarse y observar las diferencias en rendimiento. En C se utilizó la función clock() para medir el tiempo de ejecución, mientras que en Python se utilizó el módulo time.
<img width="371" height="74" alt="image" src="https://github.com/user-attachments/assets/f97fc03f-47cf-4a75-b8e8-25530ab87de7" />
<img width="469" height="74" alt="image" src="https://github.com/user-attachments/assets/bbeab5f0-3bf7-4de0-8a15-c7db02b22e7c" />
Al ejecutar el algoritmo recursivo de Fibonacci en ambos lenguajes se observaron diferencias claras en el tiempo de ejecución. En el caso del programa implementado en C, el cálculo de Fibonacci(40) tomó aproximadamente 0.858 segundos, mientras que el mismo algoritmo implementado en Python tardó alrededor de 24.02 segundos.

Esta diferencia de rendimiento se debe principalmente a que C es un lenguaje compilado, lo que significa que el código se traduce directamente a lenguaje máquina antes de ejecutarse. Esto permite que el programa se ejecute de manera más eficiente y rápida. Por otro lado, Python es un lenguaje interpretado, por lo que cada instrucción debe ser procesada por el intérprete durante la ejecución, lo que introduce una sobrecarga adicional.

Además, el algoritmo de Fibonacci utilizado es recursivo y realiza una gran cantidad de llamadas a funciones, lo que amplifica la diferencia de rendimiento entre ambos lenguajes. En conclusión, este experimento demuestra cómo el tipo de lenguaje y la forma en que se ejecuta el código pueden afectar significativamente el rendimiento de un programa.


Al comparar los resultados se puede observar que el programa escrito en C se ejecuta más rápido que el de Python. Esto ocurre porque C es un lenguaje compilado que se convierte directamente en código máquina antes de ejecutarse, mientras que Python es un lenguaje interpretado y su código se ejecuta a través de un intérprete.

Este ejercicio permitió entender mejor cómo el tipo de lenguaje y la forma en que se ejecuta el código pueden influir en el rendimiento de un programa.
