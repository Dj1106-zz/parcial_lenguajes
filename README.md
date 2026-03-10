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

En el último ejercicio se realizó una comparación entre un lenguaje compilado (C) y un lenguaje interpretado (Python). Para esto se implementó el algoritmo recursivo de Fibonacci en ambos lenguajes.

El objetivo fue medir el tiempo que tarda cada programa en ejecutarse y observar las diferencias en rendimiento. En C se utilizó la función clock() para medir el tiempo de ejecución, mientras que en Python se utilizó el módulo time.

Al comparar los resultados se puede observar que el programa escrito en C se ejecuta más rápido que el de Python. Esto ocurre porque C es un lenguaje compilado que se convierte directamente en código máquina antes de ejecutarse, mientras que Python es un lenguaje interpretado y su código se ejecuta a través de un intérprete.

Este ejercicio permitió entender mejor cómo el tipo de lenguaje y la forma en que se ejecuta el código pueden influir en el rendimiento de un programa.
