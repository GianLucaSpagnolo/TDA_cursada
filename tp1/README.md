# TRABAJO PRÁCTICO 1 - TEORÍA DE ALGORITMOS (TB024)

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

Primero que nada, se debe ejecutar el siguiente comando para darle permisos al script:

`chmod +x tests.sh`

Se disponen de los siguientes comandos para ejecutar cada uno de los tests:
  
- Ejercicio 1: `./tests.sh ej1`
- Ejercicio 2: `./tests.sh ej2`
- Ejercicio 3: `./tests.sh ej3`

Asimismo, para el ejercicio 1 y 2 se dispone del flag `-m` para ejecutar el modo manual y realizar una prueba manual.

Por ejemplo: `./tests.sh ej2 -m`

Es **importante** saber que este ultimo comando, correspondiente a la ejecucion manual del test del ejercicio 2 generara dos diferentes archivos .csv correspondientes a la disposicion final de edificios `archivo_edificios.csv` y un archivo con la disposicion de los restaurantes en la grilla en conjunto a los edificios `archivo_restaurantes.csv`

De forma alternativa, los comandos para correr cada uno de los tests sin usar el script son los siguientes:

- Ejercicio 1: `python3 ej1/ejercicio_1_test.py`
- Ejercicio 1 Manual: `python3 ej1/ejercicio_1_manual.py`
- Ejercicio 2: `python3 ej2/ejercicio_2_test.py`
- Ejercicio 2 Manual: `python3 ej1/ejercicio_2_test.py`
- Ejercicio 3: `python3 ej3/ejercicio_3_test.py`

## Update

Ahora se dispone del archivo `ejercicio_2_custom.py`. Mediante este archivo, modificando la constante `PATH_ARCHIVO` se puede utilizar un archivo .csv a eleccion con el objetivo de poder replicar casos especificos utilizando sets de datos de forma mas consistente. El comando de ejecucion es el siguiente: `python3 ej2/ejercicio_2_custom.py`. Se recomienda ejecutarlo desde el root para evitar errores.
