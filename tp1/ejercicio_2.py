MANZANA_CON_EDIFICIO = "X"
MANZANA_SIN_EDIFICIO = " "


def es_posicion_valida(mapa, x1, x2):
    try:
        mapa[x1][x2]
    except IndexError:
        return False
    if x1 < 0 or x2 < 0:
        return False
    return True


def radio_x(x, i = 0, j = 0):
    return [
        (i-x, j-x),(i-x, j),(i-x, j+x),
        ( i,  j-x),( i,  j),( i,  j+x),
        (i+x, j-x),(i+x, j),(i+x, j+x)
    ]


def obtener_a_radio_x(mapa, x, i, j, elementos_a_buscar):
    radio = []
    for x1, x2 in radio_x(x, i, j):
        if es_posicion_valida(mapa, x1, x2) and mapa[x1][x2] in elementos_a_buscar:
            coordenadas = (x1, x2)
            radio.append(coordenadas)
    return radio


def estan_a_distancia_x(mapa, x, elemento1, elemento2):
    e1x, e1y = elemento1
    e2x, e2y = elemento2
    if not es_posicion_valida(mapa, e1x, e1y) or not es_posicion_valida(mapa, e2x, e2y):
        return False
    if (e1x - e2x, e2x - e1y) not in radio_x(x):
        return False
    return True


def tiene_restaurante_a_radio_x(mapa, x, edificio, restaurantes):
    # restaurantes = reversed(restaurantes)
    for res in restaurantes:
        if estan_a_distancia_x(mapa, x, edificio, res):
            return True
    return False


def obtener_edificios(mapa):
    edificios = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            manzana = mapa[i][j]
            if manzana == MANZANA_CON_EDIFICIO:
                coordenadas = (i, j)
                edificios.append(coordenadas)
    return edificios


def manzanas_a_radio_x_del_edificio(mapa, x, edificio):
    i, j = edificio
    buscar = [MANZANA_SIN_EDIFICIO, MANZANA_CON_EDIFICIO]
    manzanas = obtener_a_radio_x(mapa, x, i, j, buscar)
    manzanas.remove(edificio)  # no se cuenta a si mismo
    return manzanas


def contar_edificios_a_radio_x_de_manzana(mapa, x, manzana):
    i, j = manzana
    buscar = [MANZANA_CON_EDIFICIO]
    edificios = obtener_a_radio_x(mapa, x, i, j, buscar)
    return len(edificios)


def max_by_value(dict_):
    max_val = max(dict_.values())
    res = list(filter(lambda x: dict_[x] == max_val, dict_))
    return res[0]


def posiciones_restaurante(mapa, x):
    edificios = obtener_edificios(mapa)
    restaurantes = []

    for edi in edificios:
        if tiene_restaurante_a_radio_x(mapa, x, edi, restaurantes):
            continue

        edificios_a_radio_x_de_manzana = {}

        for manzana in manzanas_a_radio_x_del_edificio(mapa, x, edi):
            edificios_a_radio_x_de_manzana[manzana] = contar_edificios_a_radio_x_de_manzana(mapa, x, manzana)

        manzana_max = max_by_value(edificios_a_radio_x_de_manzana)

        restaurantes.append(manzana_max)

    return restaurantes


mapa = [
    [" ","X"," "," ","X"," "],
    ["X"," "," "," "," "," "],
    [" "," "," "," "," "," "],
    ["X"," "," "," "," ","X"],
    [" "," "," ","X"," "," "],
    [" "," "," "," ","X"," "]
]

X = 1
restaurantes = posiciones_restaurante(mapa, X)


print(restaurantes)

