from time import process_time
from random import randint
import ejercicio_2 as ej2


TAMANOS_BARRIO: list = [10, 20, 40, 100, 200] # con 400 ya empieza a haber un largo tiempo de ejecución
CANTIDAD_EDIFICIOS: float = 0.2


def generar_edificios_en_grilla(tamano_barrio: int) -> list:

    cantidad_edificios: int = ej2.calcular_cantidad_edificios(tamano_barrio, CANTIDAD_EDIFICIOS)
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

        radio_de_cobertura: int = ej2.calcular_radio_de_cobertura(tamano_barrio)
        edificios: list = generar_edificios_en_grilla(tamano_barrio)

        start_time: float = process_time()
        restaurantes: list = ej2.construccion_de_restaurantes(edificios, tamano_barrio)
        end_time: float = process_time() - start_time

        print(f"\033[31;1;4mTiempo de ejecución para n = {tamano_barrio}:\033[0m {end_time:.8f} segundos")
        print(f"Cantidad de restaurantes: {len(restaurantes)} con cobertura {radio_de_cobertura}\nRestaurantes: {restaurantes}\n")


test_ej2()
