# Teoria de Algoritmos

Teoria de Algoritmos (TB024) curso 02: Echeverria

Segundo cuatrimestre 2024

Table of Contents

- [Clase 03/09](#clase-0309)

## Modalidad

Clases teorico-practicas:

- Martes de 19:00 a 22:00 presencial
- Jueves de 19:00 a 22:00 virtual sincronico

Asistencia no obligatoria, con clases grabadas.

Hay 3 **TPs** (con una fecha de recuperacion) a traves del campus virtual. Tambien, hay 1 **parcial**.

Calificacion: 50% nota del parcial y 50% del promedio de los TPs.

Lenguaje a utilizar en la materia: a eleccion.

---

## Clase 03/09

### Repaso

**Complejidad**: cuanto tarda algo, y cuantos recursos requiere. Es en base al juego de datos que utiliza.

Notacion **Big O** (ordenes de magnitud): peor escenario, cota superior del costo de memoria o tiempo, en funcion al problema. Ejemplo O(N)^2 = complejidad cuadratica. Las complejidades se comparan, y ahi se define si una es mejor o peor.

#### Estructuras de Datos

- **Arreglos** y **listas**: depende de la operacion con la que vas a usar. Una lista permite detectar formas de insercion en el medio, y manejar datos de forma dinamica. Por otro lado, un array es util cuando se maneja un conjunto fijo de elementos.
- **Diccionario** (o mapas): en base a un indice (clave) permite identificar rapidamente.
- **Hash**: permite almacenar mediante una funcion de hash, garantizando una busqueda instantanea O(1) en esta materia. Sin embargo, dandole un dato de entrada gigante, el dato de salida sera de un mismo tamaño, por lo que pueden existir dos claves que den el mismo dato: *colision*.
- **Arbol** o un ABB (Arbol Binario de Busqueda): es un grafo. No puede tener ciclos, debe tener un nodo raiz y cada nodo debe tener un padre (salvo la raiz), y se disponen de los nodos hojas (sin hijos). La ventaja frente a un hash es que un ABB (donde cada nodo tiene siempre dos hijos) esta *siempre ordenado* y no tiene problemas con colisiones.

La busqueda en un hash es O(1) mientras que en un ABB es O(log N).

- **Heap** o cola de prioridad: es una cola (FIFO). La prioridad es una funcion que permite definir a quien seleccionar primero (no necesariamente al de primera posicion, sino el que tenga mejor prioridad). El agregado de un elemento de la cola de prioridad depende de la *funcion de priorizacion* para intentar acercarse lo mas posible a O(1) al momento de ordenar la cola, pero siempre la extraccion sera O(1).

#### Grafos (repaso)

Matematicamente, es un conjunto de G(V,E) donde se poseen cadas vertices y aristas. Un ejemplo de un grafo es un camino, las redes sociales, etc.

Un grafo se puede recorrer visitando los vecinos de cada nodo. Existen formas de busqueda para recorrer los grafos: **BFS** y **DFS**.

Existen algoritmos de grafos: Prim, Kruskal, Dijkstra.

### Tecnicas de diseño

#### Division y Conquista

"Tenemos un problema, se puede resolver cada subsolucion del problema dividiendolo para resolverlo completamente al final". Es una tecnica normalmente recursiva.

La complejidad de un algoritmo DyC se calcula con el **Teorema Maestro**. Para poder insertar o recorrer en un arbol se usa DyC.

Para ordenar, su costo de ordenamiento depende del algoritmo de ordenamiento utilizado. El mejor algoritmo posible de ordenamiento tiene complejidad O(N log N). El mejor algoritmo de ordenamiento (segun la materia) es **Mergesort**.

### Demostraciones Matematicas

Pequeño repaso sobre como se pueden hacer implicaciones logicas.

Tengo H => T (H implica T)

- Si H es verdadero, T es verdadero
- Si H es falso, no importa el valor de T
- Si T es falso, entonces H es falso tambien
- Pero, si T es verdadero, H puede ser verdadero o falso

Ejemplo: si esta lloviendo llevo paraguas (H => T)

- ~T => ~H: Si no llevo paraguas, no esta lloviendo
- ~H => T v ~T: 
- 

Si H implica T, ~T implica ~H

#### ¿Como se demuestra?

- Metodo directo
- Metodo indirecto o del Contrarreciproco
- Por el absurdo o la Contradiccion
- 

##### Metodo Directo

Asume que H es verdadera, y demuestra que T debe ser verdadera.



Se usa el razonamiento de que 2 * N es par.

##### Metodo Indirecto o Contrarreciproco

Asume que T es falsa y demuestra que H es necesariamente falsa tambien.



##### Por el Absurdo o la Contradiccion

Asume que H es verdadera y que T es falsa, para luego llegar a una contradiccion.



##### Por induccion

Tiene tres pasos:

- Primero, se demuestra que H(n_0) => T(n_0) es verdadero (caso base).
- Segundo, se demuestra que H(n_n) => T(n_n)
- 

### Grafos

Grafo: *conjunto de entidades (vertices o nodos) relacionados entre si de alguna forma (aristas)*

Notacion tipica:

- G = (V,E)
- 
- 

#### Caracteristicas

- Pesados/No pesados 
- Dirigidos/No dirigidos 
- Con o sin bucles (vertice unido a si mismo con una arista)
- Simples/Compuestos 

#### Formas de Recorrido

- BFS
- DFS
- Random Walk

#### Conectividad

Dos vertices U y V estan conectados si existe una arista que los une.

**Componente**: Subgrafo en el que cualquier par de vertices esta conectado



**Grafos No Dirigidos**: Componentes conexas (todos conectados entre si). Tiene puntos de articulacion: vertices tales que, si son removidos, aumenta la cantidad de componentes conexas del grafo.



**Grafos Dirigidos**:

- Componentes fuertemente conexas: para todo par de vertices U y V, existe un camino (no confundir con arista) de U a V y de V a U. (camino de ida y vuelta)
- Componentes debilmente conexas: para todo par de vertices U y V, existe un camino de uno a otro vertice, independientemente del sentido. (camino de ida pero no de vuelta, o viceversa)



#### Orden Topologico

Es un ordenamiento de sus vertices tal que, para cada arista (U, V) que va de U hacia V, resulta que U viene antes que V.

Es un orden valido para recorrer grafos dirigidos; recorrido de un grafo donde cada nodo es visitado luego de que se visitaron todas sus dependencias.

Ejemplo: secuenciamiento de tareas (job scheduling), PERT, etc.

#### Grafos Bipartitos

Grafos en el que sus vertices se pueden dividir en dos subconjuntosdisjuntos e independientes U y V, tales que toda arista conecta un elemento de U con uno de V (y nada mas).

Un grafo es **completo** cuando todos los elementos estan conectados por aristas entre si. Po otro lado, un grafo es **K_mn completo** cuando todos los elementos de U tienen aristas que los unen con todos los elementos de V, con m y n vertices respectivamente.



Un grafo es bipartito *si y solo si no tiene caminos impares*

##### Distancia

Grafos no pesados: usamos BFS porque es O(N)

Grafos pesados: si todos los pesos son positivos, usamos Dijkstra. Sino, podemos usar Bellman-Ford. 

#### Arbol de Tendido Minimo

**Arbol de tendido**: Dado un grafo no dirigido G, es un subgrafo que ademas es un arbol. Incluye todos los vertices del grafo.

**Arbol de tendido minimo**: Dado un grafo pesado G, es un arbol de tendido de G tal que su peso es el minimo. *Algoritmo de Prim y Kruskal*. Solo tiene sentido hablar de un Arbol de Tendido minimo cuando se trata de un grafo pesado.

#### Representacion de un Grafo

- **Matriz de Adyacencia**: mide cuantas aristas hay entre cada par de vertices.
  - Es cuadrada: V x V
  - Si el grafo no es dirigido, es simetrica
  - Si no hay bucles, la diagonal principal son todos ceros.
- **Lista de Adyacencia**: lista de todas las aristas. (conjunto E que define a un grafo)
- **Matriz de Incidencia** (se usa muy poco): mide si existe o no una arista entre cada par de vertices.

##### Potenciacion de la Matriz de Adyacencia

Sea A la matriz de adyacencia de un grafo (dirigido o no). Entonces el elemento a_ij denota si dos vertices (i,j) son adyacentes o no.

**Teorema**: A ^ n (el producto de matrices de A consigo misma n veces) resulta en una matriz cuyo elemento A_ij ^ n 

**Demostracion** (por induccion):


