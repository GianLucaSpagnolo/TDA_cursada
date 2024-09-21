import math

def calcular_cobertura(edificio, edificios, radio, n):
    cx, cy = edificio
    x1, x2 = max(cx - radio, 0), min(cx + radio, n-1)
    y1, y2 = max(cy - radio, 0), min(cy + radio, n-1)
    return {(x, y) for x, y in edificios if x1 <= x <= x2 and y1 <= y <= y2}

def greedy(edificios, n):
    edificios = set(edificios)
    restaurantes = set()
    radio = math.ceil(0.2 * n)

    while edificios:
        max_cobertura = 0
        mejor_edificio = None
        mejor_cobertura = None

        for edificio in edificios:
            cobertura = calcular_cobertura(edificio, edificios, radio, n)
            if len(cobertura) > max_cobertura:
                max_cobertura = len(cobertura)
                mejor_edificio = edificio
                mejor_cobertura = cobertura

        restaurantes.add(mejor_edificio)
        edificios -= mejor_cobertura

    return restaurantes