import random

POSIBLES_COLORES = [1, 2, 3] # Colores posibles para colorear los vertices
CANTIDAD_ARISTAS_SATISFECHAS = 2/3 # Cantidad minima de aristas satisfechas necesarias


def obtener_aristas_satisfechas_minimas(cantidad_aristas) -> int:
    return cantidad_aristas * CANTIDAD_ARISTAS_SATISFECHAS


def problema_3_coloreo_aleatorio(grafo, limite):
    """
    Algoritmo randomizado para 3-Coloreo optimizado.
    
    Argumentos:
        grafo (diccionario): Es un grafo representado como un diccionario, cuyas claves son los vertices y los valores son listas de vecinos
        limite (numero entero): Corresponde a la cantidad minima de aristas satisfechas necesarias
    """
    mejor_asignacion = {} # Mejor asignacion de color para cada vertice
    max_aristas_satisfechas = 0 # Cantidad maxima de aristas satisfechas
    
    while max_aristas_satisfechas < limite:
        asignacion = {}
        aristas_satisfechas = 0
        
        for v in grafo:
            asignacion[v] = random.choice(POSIBLES_COLORES) # Asignar un color aleatorio a cada vertice de entre 3 opciones

        for v in grafo:
            for u in grafo[v]:
                if asignacion[v] != asignacion[u]:
                    aristas_satisfechas += 1
        aristas_satisfechas //= 2 # Grafo no dirigido, no se cuentan las aristas dos veces

        if aristas_satisfechas > max_aristas_satisfechas:
            mejor_asignacion = asignacion
            max_aristas_satisfechas = aristas_satisfechas
    
    return mejor_asignacion, max_aristas_satisfechas
