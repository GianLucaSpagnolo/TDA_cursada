# TRABAJO PRÁCTICO 2 - TEORÍA DE ALGORITMOS (TB024)

2º Cuatrimestre 2024
Grupo: 5 (She Don’t Give Grafo)
Curso 03 - Echevarría

## Integrantes

- Pablo Choconi - 106388
- Valentín Savarese - 107640
- Gian Luca Spagnolo - 108072
- Brian Céspedes - 108219
- Néstor Palavecino - 108244

## Guia de Uso de los Tests

### Ejercicio 1

Para el **Ejercicio 1** se dispone del archivo `ejercicio_1_test.py` el cual permite leer un archivo .csv para identificar trabajos tanto tranquilos como estresantes, y asi poder ejecutar nuestras dos implementaciones de este problema: `ejercicio_1.py` (con lista de optimos) y `ejercicio_1_sin_lista_de_opt.py` (sin lista de optimos), mostrando la diferencia de los tiempos de ejecucion de ambos algoritmos.

**Comando para ejecutar el archivo de test** (desde el directorio TP2): `python3 ej1/ejercicio_1_test.py`

En caso de querer incluir tests adicionales, se puede agregar un archivo .csv al directorio `res` presente en la carpeta del ejercicio 1, y se debe modificar el archivo `ejercicio_1_test.py` agregando como constante global `PATH_ARCHIVO` con el path correspondiente al nuevo archivo .csv ingresado. El formato del archivo .csv debe ser el siguiente:

- Columna 0: Numero de trabajo
- Columna 1: Trabajo tranquilo
- Columna 2: Trabajo estresante

Asimismo, para este ejercicio se disponen de numerosos archivos .csv ingresados previamente con datasets de hasta 10000 entradas, para poder visualizar diferentes resultados y tiempos de ejecucion con determinados conjuntos de datos.

### Ejercicio 2



### Ejercicio 3

Para ejecutar el archivo `ejercicio_3.bas` se debe tener instalado **PCBASIC**.

Documentacion: <https://robhagemans.github.io/pcbasic/>

Instalacion en Linux: `pip3 install pcbasic`

Para poder ejecutar el archivo en este interprete, se debe usar el siguiente comando (desde el directorio TP2): `pcbasic ej3/ejercicio_3.bas`

Ademas, en el mismo directorio correspondiente a este ejercicio, se dispone del archivo `ejercicio_3_refactor.bas`, el cual implementa el mismo algoritmo brindado en el enunciado, pero modularizado, refactorizado y documentado para una mayor comprension, organizacion, mantenibilidad y desempeño.
