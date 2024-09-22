import numpy as np
from time import time
import random

def generar_mapa(n, probabilidad_edificio=0.2):
    """Genera un mapa de nxn con edificios distribuidos aleatoriamente."""
    return np.random.choice([0, 1], size=(n, n), p=[1-probabilidad_edificio, probabilidad_edificio])

def distancia(manzana1, manzana2):
    """Calcula la distancia Manhattan entre dos manzanas."""
    return abs(manzana1[0] - manzana2[0]) + abs(manzana1[1] - manzana2[1])

def encontrar_mejor_manzana(mapa, edificios_no_cubiertos, X):
    """Encuentra la mejor manzana para colocar un restaurante de acuerdo a la regla greedy."""
    n = len(mapa)
    max_cubre = 0
    mejor_manzana = None
    
    for i in range(n):
        for j in range(n):
            cubre = sum(1 for edificio in edificios_no_cubiertos 
                        if distancia((i, j), edificio) <= X)
            if cubre > max_cubre:
                max_cubre = cubre
                mejor_manzana = (i, j)
    
    return mejor_manzana

def greedy_restaurantes(mapa, X):
    """Implementa el algoritmo greedy para minimizar la cantidad de restaurantes."""
    n = len(mapa)
    edificios = [(i, j) for i in range(n) for j in range(n) if mapa[i][j] == 1]
    edificios_no_cubiertos = set(edificios)
    restaurantes = []
    
    while edificios_no_cubiertos:
        mejor_manzana = encontrar_mejor_manzana(mapa, edificios_no_cubiertos, X)
        restaurantes.append(mejor_manzana)
        edificios_cubiertos = [edificio for edificio in edificios_no_cubiertos 
                               if distancia(mejor_manzana, edificio) <= X]
        edificios_no_cubiertos -= set(edificios_cubiertos)
    
    return restaurantes

def prueba(n, X):
    """Ejecuta una prueba con un mapa de tamaño n y cobertura X."""
    mapa = generar_mapa(n)
    print(f"Mapa de {n}x{n} generado con edificios (1) y vacíos (0):\n{mapa}\n")
    time_start = time()
    restaurantes = greedy_restaurantes(mapa, X)
    time_end = time() - time_start
    print(f"Tiempo de ejecución: {time_end:.8f} segundos")
    print(f"Restaurantes necesarios: {len(restaurantes)}")
    print(f"Ubicaciones de los restaurantes: {restaurantes}")

# Ejemplo de prueba
n = 40
X = n ** 0.2
prueba(n, X)
