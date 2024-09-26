from time import time
from random import randint
import ejercicio_2 as ej2


TAMANOS_BARRIO: list = [10, 20, 50, 100, 200, 300] # con 400 ya empieza a haber problemas... Pueden verificarlo
CANTIDAD_EDIFICIOS: float = 0.2


def generar_edificios_en_grilla(tamano_barrio: int) -> list:

    cantidad_edificios: int = round(tamano_barrio ** 2 * CANTIDAD_EDIFICIOS)
    edificios: list = list()

    for _ in range(cantidad_edificios):
        while True:
            edificio = (randint(0, tamano_barrio - 1), randint(0, tamano_barrio - 1))
            if edificio not in edificios:
                edificios.append(edificio)
                break

    return edificios


def test_ej2() -> None:

    for tamano_barrio in TAMANOS_BARRIO:

        edificios: list = generar_edificios_en_grilla(tamano_barrio)

        start_time: float = time()
        restaurantes: list = ej2.construccion_de_restaurantes(edificios, tamano_barrio)
        end_time: float = time() - start_time

        print(f"Tiempo de ejecución para n = {tamano_barrio}: {end_time} segundos\n")

        print(f"Cantidad de restaurantes: {len(restaurantes)}\nRestaurantes: {restaurantes}\n")


test_ej2()
