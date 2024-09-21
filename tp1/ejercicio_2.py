def dentro_rango(otro_edificio, edificio_central, radio, n):
    cx, cy = edificio_central

    x1 = max(cx - radio, 0)
    x2 = min(cx + radio, n-1)

    y1 = max(cy - radio, 0)
    y2 = min(cy + radio, n-1)

    x, y = otro_edificio

    return (x1 <= x <= x2) and (y1 <= y <= y2)


def calcular_cobertura(edificios, edificio_central, radio, n) -> list[int, list[list[int, int]]]:
    cobertura = set()

    for edificio in edificios:
        if dentro_rango(edificio, edificio_central, radio, n):
            cobertura.add(edificio)

    return cobertura


def greedy(edificios, n):
    
    edificios_visitados = set()
    restaurantes = set()
    diccionario_edificios = dict()

    x = round(0.2 * n)


    for edificio in edificios:
        edificios_en_rango = calcular_cobertura(edificios, edificio, x, n)
        diccionario_edificios[edificio] = edificios_en_rango

    while len(diccionario_edificios) > 0:

        max_cobertura = 0
        edificios_cubiertos = None
        edificio_max_cobertura = None

        for edificio in diccionario_edificios:

            cobertura = diccionario_edificios[edificio]

            if len(cobertura) > max_cobertura:
                max_cobertura = len(cobertura)
                edificios_cubiertos = cobertura
                edificio_max_cobertura = edificio

        edificios_visitados.update(edificios_cubiertos)
        restaurantes.add(edificio_max_cobertura)
    
        for e in set(diccionario_edificios.keys()):
            if e in edificios_cubiertos:
                del diccionario_edificios[e]
            else:
                diccionario_edificios[e] -= edificios_cubiertos

    return restaurantes
