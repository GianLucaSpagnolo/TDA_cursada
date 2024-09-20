import math


def marcar_edificios_visitados(edificios_visitados, edificios_cubiertos):
    for e in edificios_cubiertos:
        edificios_visitados.append(e)


def dentro_rango(otro_edificio, edificio_central, radio, n):
    cx, cy = edificio_central

    x1 = max(cx - radio, 0)
    x2 = min(cx + radio, n-1)

    y1 = max(cy - radio, 0)
    y2 = min(cy + radio, n-1)

    x, y = otro_edificio

    return (x1 <= x <= x2) and (y1 <= y <= y2)


def calcular_cobertura(edificios, edificios_visitados, edificio, radio, n) -> list[int, list[list[int, int]]]:
    cobertura = []

    for e in edificios:
        if e in edificios_visitados:
            continue
        if dentro_rango(e, edificio, radio, n):
            cobertura.append(e)

    return len(cobertura), cobertura


def greedy(edificios, n):
    edificios_visitados = []
    restaurantes = []

    x = math.ceil(0.2 * n)

    while len(edificios_visitados) < len(edificios):
        max_cobertura = -1
        edificios_cubiertos = None
        edificio_max_cobertura = None

        for edificio in edificios:
            if edificio in edificios_visitados:
                continue

            (cobertura, edificios_dentro_de_cobertura) = calcular_cobertura(edificios, edificios_visitados, edificio, radio=x, n=n)

            if cobertura > max_cobertura:
                max_cobertura = cobertura
                edificios_cubiertos = edificios_dentro_de_cobertura
                edificio_max_cobertura = edificio

        marcar_edificios_visitados(edificios_visitados, edificios_cubiertos)
        restaurantes.append(edificio_max_cobertura)

    return restaurantes


# edificios = [
#     (0,0),
#     (0,5),
#     (1,2),
#     (1,6),
#     (2,5),
#     (2,8),
#     (3,3),
#     (3,6),
#     (4,0),
#     (5,2),
#     (5,5),
#     (6,4),
#     (6,7),
#     (7,1),
#     (7,4),
#     (8,7)
# ]

# restaurantes = greedy(edificios, n = 9)
# result_len = len(restaurantes)

# # (5,2), (1,6), (6,7), (0,0)
# print(restaurantes)
# print(result_len)

# assert result_len == 4
