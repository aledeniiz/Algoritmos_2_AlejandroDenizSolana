# Algoritmos_2_AlejandroDenizSolana
1.Ejercicio POO (Genre):
Este ejercicio se centra en la implementación de una estructura de clases en Python para modelar canciones y géneros musicales, 
así como en la utilización de la clase Enum y la herramienta functools.partial.

Clase Genre: Se define una enumeración Genre que representa los distintos géneros musicales. Cada género se representa como una 
constante con un valor asociado que es una cadena de caracteres.
Clase Song: Se implementa una clase Song que representa una canción y sus atributos como nombre, artista, duración, fecha de 
lanzamiento y géneros. La clase incluye métodos para obtener y establecer estos atributos, así como para añadir géneros a la 
canción, comparar canciones y representarlas como cadenas de caracteres.
Uso de functools.partial: Se utiliza la herramienta functools.partial para crear versiones especializadas de los métodos de 
la clase SimpleOperations con descuentos y tasas de impuestos predefinidos. Esto permite aplicar descuentos y calcular impuestos
de manera más específica y conveniente en diferentes contextos.
Pruebas unitarias: Se incluye una función main() para probar la clase Genre con casos de prueba que verifican si los géneros 
están correctamente definidos como instancias de la enumeración Genre.
En resumen, este ejercicio demuestra habilidades en la creación de clases, el uso de enumeraciones, la aplicación de decoradores 
como functools.partial y la realización de pruebas unitarias en Python. Además, muestra comprensión de conceptos fundamentales de 
la programación orientada a objetos y buenas prácticas de programación.


Ejercicio 2 Recursividad: Calculo Factorial:
Esta solución implementa el cálculo del factorial de un número utilizando recursividad. La función factorial(n) toma un número 
entero n como entrada y devuelve su factorial. La documentación proporcionada describe los parámetros y el valor de retorno de 
la función, junto con un ejemplo de uso.

El algoritmo utiliza un enfoque recursivo para calcular el factorial. Si el número dado es 0, el factorial es 1 (caso base). Para 
números mayores que 0, se realiza un paso recursivo multiplicando el número por el factorial del número anterior (n-1). Esto se 
repite hasta que se alcanza el caso base.

La función main() se utiliza para probar la función factorial(), mostrando el resultado del factorial de 5 como ejemplo de uso.

En resumen, esta solución demuestra un conocimiento sólido de la recursividad y su aplicación en el cálculo del factorial, además 
de proporcionar una documentación clara y un ejemplo de uso para comprender mejor su funcionamiento.


# Cálculo del Factorial de un Número Mediante Recursividad

Este programa en Python calcula el factorial de un número entero no negativo de manera recursiva. El factorial de un número entero no negativo 𝑛, denotado como 𝑛!, es el producto de todos los enteros positivos menores o iguales a 𝑛. Por ejemplo:
- 5! = 5 × 4 × 3 × 2 × 1 = 120

## Funcionamiento del Código

La función `factorial` acepta un único parámetro: el número entero 𝑛.
- Caso Base: Si 𝑛 es 0, entonces 0! = 1 por definición. Este será el caso base si 𝑛 = 0, retorna 1.
- Paso Recursivo: Si 𝑛 > 0, la función retorna 𝑛 × factorial(n-1).

Ejercicio 3 Ordenacion:
Bubble Sort

Bubble Sort, también conocido como Ordenamiento Burbuja, es un algoritmo de ordenación simple que funciona recorriendo repetidamente la lista de elementos a ordenar. En cada paso, compara los elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que no se requieren más intercambios, lo que indica que la lista está ordenada.

Funcionamiento del Bubble Sort

Se comienza comparando el primer elemento con el segundo.
Si el primer elemento es mayor que el segundo, se intercambian.
Se pasa al siguiente par de elementos adyacentes y se repite el proceso hasta llegar al final de la lista.
Luego, se repite todo el proceso para cada elemento de la lista, desde el principio hasta el final.
Este proceso se repite hasta que no se realicen más intercambios en ninguna iteración, lo que indica que la lista está ordenada.
Casos de uso

Bubble Sort es útil para ordenar pequeñas cantidades de elementos o cuando la simplicidad y la claridad del código son más importantes que la eficiencia. Sin embargo, para conjuntos de datos grandes, Bubble Sort tiende a ser menos eficiente que otros algoritmos de ordenación más avanzados, como Quick Sort o Merge Sort.

Ejemplo de Aplicación de Bubble Sort

Supongamos que tenemos la siguiente lista de números: [34, 7, 23, 32, 5]. Aplicamos el algoritmo Bubble Sort para ordenarla:

Pasada 1:
Comparamos 34 y 7, los intercambiamos: [7, 34, 23, 32, 5]
Comparamos 34 y 23, no se intercambian: [7, 34, 23, 32, 5]
Comparamos 34 y 32, no se intercambian: [7, 34, 23, 32, 5]
Comparamos 34 y 5, los intercambiamos: [7, 23, 32, 5, 34]
Pasada 2:
Comparamos 7 y 23, no se intercambian: [7, 23, 32, 5, 34]
Comparamos 23 y 32, no se intercambian: [7, 23, 32, 5, 34]
Comparamos 32 y 5, los intercambiamos: [7, 23, 5, 32, 34]
Pasada 3:
Comparamos 7 y 23, no se intercambian: [7, 23, 5, 32, 34]
Comparamos 23 y 5, los intercambiamos: [7, 5, 23, 32, 34]
Pasada 4:
Comparamos 7 y 5, los intercambiamos: [5, 7, 23, 32, 34]
La lista ahora está ordenada: [5, 7, 23, 32, 34].

Ejercicio 4 Functools:
Este ejercicio demuestra la aplicación de la herramienta functools.partial en Python para la configuración parcial de argumentos de funciones.

La clase SimpleOperations implementa dos métodos: apply_discount para aplicar descuentos a precios y calculate_tax para calcular impuestos sobre 
precios dados. Utilizando functools.partial, se configuran versiones especializadas de estos métodos con descuentos y tasas de impuestos predefinidos.

La configuración parcial de funciones permite la reutilización eficiente de código y la creación de funciones especializadas para casos específicos, 
lo que mejora la legibilidad y mantenibilidad del código. En este caso, se han creado funciones preconfiguradas twenty_percent_discount y vat_tax para 
aplicar un descuento del 20% y un impuesto del 21%, respectivamente, sobre un precio dado.

El ejercicio ilustra cómo functools.partial puede simplificar el desarrollo de aplicaciones al permitir la creación de funciones más expresivas y 
específicas para diferentes situaciones, lo que contribuye a un código más limpio y modular.





