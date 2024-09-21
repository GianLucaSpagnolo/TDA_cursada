import math
from ordered_set import OrderedSet


def calcular_cobertura2(edificio, edificios, radio, n):
    cx, cy = edificio
    x1, x2 = max(cx - radio, 0), min(cx + radio, n-1)
    y1, y2 = max(cy - radio, 0), min(cy + radio, n-1)
    return OrderedSet([(x, y) for x, y in edificios if x1 <= x <= x2 and y1 <= y <= y2])


def greedy2(edificios, n):
    edificios = OrderedSet(edificios)
    restaurantes = list()
    radio = math.ceil(0.2 * n)

    while len(edificios) > 0:
        max_cobertura = -1
        mejor_edificio: tuple = None
        mejor_cobertura: OrderedSet = None

        for edificio in edificios:
            cobertura = calcular_cobertura2(edificio, edificios, radio, n)
            if len(cobertura) > max_cobertura:
                max_cobertura = len(cobertura)
                mejor_edificio = edificio
                mejor_cobertura = cobertura

        restaurantes.append(mejor_edificio)
        edificios -= mejor_cobertura

    return restaurantes
