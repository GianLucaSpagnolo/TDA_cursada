from time import time
from random import randint
import ejercicio_2 as ej2


N = [10, 20, 50, 100]
CANTIDAD_EDIFICIOS = 0.2


def generar_edificios_en_grilla(n):
    cantidad_edificios = int(n * n * CANTIDAD_EDIFICIOS)
    edificios = []
    for _ in range(cantidad_edificios):
        while True:
            edificio = (randint(0, n - 1), randint(0, n - 1))
            if edificio not in edificios:
                edificios.append(edificio)
                break
    return edificios


def test_ej2():
    for n in N:
        edificios = generar_edificios_en_grilla(n)
        #for i in range(n):
        #    print(" ".join(["E" if (i, j) in edificios else "." for j in range(n)]))

        start_time = time()
        restaurantes = ej2.greedy(edificios, n)
        end_time = time() - start_time
        print(f"Tiempo de ejecución para n={n}: {end_time} segundos\n")

        print(f"Cantidad de restaurantes: {len(restaurantes)}\nRestaurantes: {restaurantes}\n")


test_ej2()
