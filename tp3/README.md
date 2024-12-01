# TRABAJO PRÁCTICO 3 - TEORÍA DE ALGORITMOS (TB024)

2º Cuatrimestre 2024
Grupo: 5 (She Don’t Give Grafo)
Curso 03 - Echevarría

## Integrantes

- Pablo Choconi - 106388
- Valentín Savarese - 107640
- Gian Luca Spagnolo - 108072
- Brian Céspedes - 108219
- Néstor Palavecino - 108244

## Guia de Uso de las Implementaciones

### Ejercicio 1

Se dispone en el archivo `ejercicio_1.py` de la implementacion del algoritmo randomizado correspondiente al problema de 3-Coloreo. En el archivo `ejercicio_1_test.py` se encuentran los tests correspondientes de nuestra implementacion, para verificar los tiempos de ejecucion del algoritmo.

Para correr el programa de testeo del algoritmo, se necesita correr el siguiente comando:

    python ej1/ejercicio_1_test.py

Por favor, ejecutar los tests desde el directorio root del TP3 (`/tp3`).

Estos tests utilizan archivos de testeo en formato .csv ubicados en el directorio `ej1/res`. En caso de querer agregar un test personalizado, se puede crear un archivo .csv en ese mismo directorio, y cambiar la constante global `PATH_ARCHIVO` del archivo `ejercicio_1_test.py`.

El formato del archivo .csv debe ser el siguiente:

    numero_de_vertice,arista_1,arista_2,...,arista_n

Recordar que, al tratarse de un problema que utiliza grafos no dirigidos, es necesario que cada arista este presente en ambos vertices correspondientes. Ver los archivos presentes en el directorio `ej1/res` para encontrar ejemplos de archivos ya creados.

### Ejercicio 2


