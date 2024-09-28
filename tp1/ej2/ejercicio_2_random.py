from time import process_time
from random import randint, seed
import ejercicio_2 as ej2


N: list = [10, 20, 50]
CANTIDAD_EDIFICIOS: float = 0.2

# Semilla para generar los edificios
# Cambiar la semilla para obtener diferentes grillas de edificios
SEMILLA = 5000


def print_edificios_en_grilla(edificios: list, tamano_barrio: int) -> None:
    for i in range(tamano_barrio):
        for j in range(tamano_barrio):
            if (i, j) in edificios:
                print("■", end=" ")
            else:
                print("·", end=" ")
        print()
    print()


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
    seed(SEMILLA)

    for tamano_barrio in N:
        print(f"\033[31;1;4mMatriz de tamaño NxN con N = {tamano_barrio}\033[0m\nGrilla de edificios (Edificio = ■)\n")
        restaurantes: list = list()
        edificios: list = generar_edificios_en_grilla(tamano_barrio)
        print_edificios_en_grilla(edificios, tamano_barrio)

        start_time = process_time()
        restaurantes = ej2.construccion_de_restaurantes(edificios, tamano_barrio)
        end_time = process_time() - start_time

        print(f"\nTiempo de ejecución para n = {tamano_barrio}: {end_time:.8f} segundos")
        print(f"Cantidad de restaurantes: {len(restaurantes)} con cobertura {round(ej2.RADIO_DE_COBERTURA * tamano_barrio)}")
        print(f"Restaurantes: {restaurantes}\n")


test_ej2()
