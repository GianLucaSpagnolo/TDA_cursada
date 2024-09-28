from time import process_time
from random import randint
import ejercicio_2 as ej2


TAMANOS_BARRIO: list = [10, 20, 50, 100, 200] # con 400 ya empieza a haber problemas en cuanto a tiempo... Pueden verificarlo
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

        start_time = process_time()
        restaurantes: list = ej2.construccion_de_restaurantes(edificios, tamano_barrio)
        end_time = process_time() - start_time

        print(f"\033[31;1;4mTiempo de ejecución para n = {tamano_barrio}:\033[0m {end_time:.8f} segundos")
        print(f"Cantidad de restaurantes: {len(restaurantes)} con cobertura {round(ej2.RADIO_DE_COBERTURA * tamano_barrio)}\nRestaurantes: {restaurantes}\n")


test_ej2()
