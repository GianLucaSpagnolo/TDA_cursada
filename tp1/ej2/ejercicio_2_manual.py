from time import process_time
from random import randint
import ejercicio_2 as ej2


CANTIDAD_EDIFICIOS: float = 0.2


def print_edificios_en_grilla(edificios: list, tamano_barrio: int, archivo) -> None:
    for i in range(tamano_barrio):
        for j in range(tamano_barrio):
            if (i, j) in edificios:
                archivo.write("E,")
            else:
                archivo.write(" ,")
        archivo.write("\n")

def print_edificios_y_restaurantes_en_grilla(edificios: list, restaurantes: list, tamano_barrio: int, archivo) -> None:
    for i in range(tamano_barrio):
        for j in range(tamano_barrio):
            if (i, j) in edificios and (i, j) not in restaurantes:
                archivo.write("E,")
            elif (i, j) in restaurantes:
                archivo.write("R,")
            else:
                archivo.write(" ,")
        archivo.write("\n")


def generar_edificios_en_grilla(tamano_barrio: int, edificios: list) -> list:
    cantidad_edificios: int = ej2.calcular_cantidad_edificios(tamano_barrio, CANTIDAD_EDIFICIOS)

    for _ in range(cantidad_edificios):
        if edificios and len(edificios) == cantidad_edificios:
            break

        while True:
            edificio = (randint(0, tamano_barrio - 1), randint(0, tamano_barrio - 1))
            if edificio not in edificios:
                edificios.append(edificio)
                break

    return edificios


def test_ej2() -> None:

    print("Por favor, selecciona un tamaño del mapa a generar para el barrio.")
    print("Se generará una grilla con N x N cantidad de cuadras.")
    print("(Se recomienda un valor de N menor a 300 para poder manejar la complejidad)")

    n: int = 10
    try:
        n: int = int(input("Ingrese el tamaño del barrio (N): "))
    except ValueError:
        print(f"Valor por defecto: {n}")

    print(f"\n\033[31;1;4mMatriz de tamaño {n}x{n}\033[0m\n")

    radio_cobertura = ej2.calcular_radio_de_cobertura(n)
    print(f"Se colocaran {ej2.calcular_cantidad_edificios(n, CANTIDAD_EDIFICIOS)} edificios en posiciones aleatorias (20% de N * N = {n * n} cuadras)")
    print(f"Radio de cobertura: {radio_cobertura} (20% de {n}) (cobertura radial)\n")

    modo_manual = False
    try:
        modo_manual = input("¿Desea colocar manualmente los edificios? (y/n): ").lower() == "y"
    except ValueError:
        print("Valor por defecto: No")


    archivo_edificios = open("archivo_edificios.csv", "w")
    archivo_restaurantes = open("archivo_restaurantes.csv", "w")

    edificios: list = []
    if modo_manual:
        while True:
            try:
                x: int = int(input(f"Ingrese la coordenada X del edificio (menor a {n}): "))
                y: int = int(input(f"Ingrese la coordenada Y del edificio (menor a {n}): "))
                if (x, y) in edificios:
                    print("Ya existe un edificio en esa posición. Intente nuevamente.\n")
                    continue
                if x < 0 or x >= n or y < 0 or y >= n:
                    print("Coordenadas fuera de rango. Intente nuevamente.\n")
                    continue

                edificios.append((x, y))

                if len(edificios) == ej2.calcular_cantidad_edificios(n, CANTIDAD_EDIFICIOS):
                    break
                print(f"Edificio colocado en la posición ({x}, {y}). Quedan {ej2.calcular_cantidad_edificios(n, CANTIDAD_EDIFICIOS) - len(edificios)} edificios por colocar.\n")
                
                valor: str = str(input("¿Desea colocar otro edificio? (y/n): ")).lower()
                if valor == "n":
                    break

            except ValueError:
                print("Valores no válidos. Intente nuevamente.\n")

    restaurantes: list = list()
    edificios: list = generar_edificios_en_grilla(n, edificios)
    print_edificios_en_grilla(edificios, n, archivo_edificios)

    start_time: float = process_time()
    restaurantes = ej2.construccion_de_restaurantes(edificios, n)
    end_time: float = process_time() - start_time

    print(f"\nTiempo de ejecución para n = {n}: {end_time:.8f} segundos")
    print(f"Cantidad de restaurantes: {len(restaurantes)} con radio de cobertura = {radio_cobertura}")
    print(f"Restaurantes: {restaurantes}\n")
    print_edificios_y_restaurantes_en_grilla(edificios, restaurantes, n, archivo_restaurantes)

    archivo_edificios.close()
    archivo_restaurantes.close()

test_ej2()
