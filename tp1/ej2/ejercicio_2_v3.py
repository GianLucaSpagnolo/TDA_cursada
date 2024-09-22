
PORCENTAJE_EDIFICIOS = 0.2

def calcular_radio_cobertura(n):
    return n * PORCENTAJE_EDIFICIOS

def verificar_distancia_manhattan(ubicacion_manzana, edificios, cobertura):
    edificios_cercanos = []
    for edificio in edificios:
        if abs(edificio[0] - ubicacion_manzana[0]) + abs(edificio[1] - ubicacion_manzana[1]) <= cobertura:
            edificios_cercanos.append(edificio)
    return edificios_cercanos

def greedy(edificios, n):
    manzanas_cubiertas: dict = {}
    cobertura = calcular_radio_cobertura(n)

    # O(n)
    for i in range(n):
        # O(n)
        for j in range(n):
            # O(k)
            cobertura_manzana = ((i, j), verificar_distancia_manhattan((i, j), edificios, cobertura))
            cantidad_edificios_cerca = len(cobertura_manzana[1])

            # O(1)
            if cantidad_edificios_cerca > 0:
                manzanas_cubiertas.setdefault(cantidad_edificios_cerca, []).append(cobertura_manzana)
    
    restaurantes = []
    edificios_restantes = len(edificios)

    for i, cantidad_edificios_cerca in enumerate(sorted(manzanas_cubiertas.keys(), reverse=True)):
        if edificios_restantes == 0:
            break

        for j, manzana in enumerate(manzanas_cubiertas[cantidad_edificios_cerca]):
            if edificios_restantes == 0:
                break

            hay_edificios_sin_cubrir = False
            for edificio in manzana[1]:
                if edificio in edificios:
                    hay_edificios_sin_cubrir = True
                    edificios.remove(edificio)
                    edificios_restantes -= 1

            if hay_edificios_sin_cubrir:
                restaurantes.append(manzana[0])

    return restaurantes
