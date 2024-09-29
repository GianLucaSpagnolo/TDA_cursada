# Guia de uso de los tests de este TP

Primero que nada, se debe ejecutar el siguiente comando para darle permisos al script:

`chmod +x tests.sh`

Se disponen de los siguientes comandos para ejecutar cada uno de los tests:
  
- Ejercicio 1: `./tests.sh ej1`
- Ejercicio 2: `./tests.sh ej2`
- Ejercicio 3: `./tests.sh ej3`

Asimismo, para el ejercicio 1 y 2 se dispone del flag `-m` para ejecutar el modo manual y realizar una prueba manual.

Por ejemplo: `./tests.sh ej2 -m`

Es **importante** saber que este ultimo comando, correspondiente a la ejecucion manual del test del ejercicio 2 generara dos diferentes archivos .csv correspondientes a la disposicion final de edificios `archivo_edificios.csv` y un archivo con la disposicion de los restaurantes en la grilla en conjunto a los edificios `archivo_restaurantes.csv`
