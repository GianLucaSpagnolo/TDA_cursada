RADIO_DE_COBERTURA: int = 0.20

def calcular_radio_de_cobertura(tamano_barrio: int) -> int:
    return round(RADIO_DE_COBERTURA * tamano_barrio)

def calcular_cantidad_edificios(tamano_barrio: int, cantidad_edificios: int) -> int:
    return round(tamano_barrio ** 2 * cantidad_edificios)


def calcular_cobertura(edificio_central: tuple, edificios: list, radio_de_cobertura: int, tamano_barrio: int) -> set:
    """
    Calcula la cobertura de un edificio central en base a su radio de cobertura.
    
    Se tiene en cuenta la cobertura en base a la distancia radial.
    """

    cobertura: set = set()
    coordenada_x_punto_central: int = edificio_central[0]
    coordenada_y_punto_central: int = edificio_central[1]

    limite_izquierdo: int = max(coordenada_x_punto_central - radio_de_cobertura, 0)
    limite_derecho: int = min(coordenada_x_punto_central + radio_de_cobertura, tamano_barrio - 1)
    limite_superior: int = max(coordenada_y_punto_central - radio_de_cobertura, 0)
    limite_inferior: int = min(coordenada_y_punto_central + radio_de_cobertura, tamano_barrio - 1)

    for x, y in edificios:
        if (limite_izquierdo <= x <= limite_derecho) and (limite_superior <= y <= limite_inferior):
            cobertura.add((x, y))

    return cobertura


def crear_diccionario_edificios(edificios: list, tamano_barrio: int) -> dict:

    diccionario_edificios: dict = dict()
    radio_de_cobertura: int = calcular_radio_de_cobertura(tamano_barrio)
    edificios.sort()

    for edificio in edificios:
        cobertura: set = calcular_cobertura(edificio, edificios, radio_de_cobertura, tamano_barrio)
        diccionario_edificios[edificio] = cobertura

    return diccionario_edificios


def eliminar_edificios_cubiertos(diccionario_edificios: dict, edificios_ya_cubiertos: set) -> None:

    for edificio_ya_visitado in edificios_ya_cubiertos:
        del diccionario_edificios[edificio_ya_visitado]

    for edificio in diccionario_edificios:
        diccionario_edificios[edificio] -= edificios_ya_cubiertos


def construccion_de_restaurantes(edificios: list, tamano_barrio: int) -> list:

    restaurantes: list = list()
    diccionario_edificios: dict = crear_diccionario_edificios(edificios, tamano_barrio)

    while diccionario_edificios:
        max_cobertura: int = 0
        mejor_edificio: tuple = ()
        mejor_cobertura: set = set()

        for edificio, cobertura in diccionario_edificios.items():
            if len(cobertura) > max_cobertura:
                max_cobertura = len(cobertura)
                mejor_edificio = edificio
                mejor_cobertura = cobertura

        restaurantes.append(mejor_edificio)
        eliminar_edificios_cubiertos(diccionario_edificios, mejor_cobertura)

    return restaurantes
