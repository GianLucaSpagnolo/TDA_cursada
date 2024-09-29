from time import process_time

import ejercicio_1 as ej1

MONEDA_NORMAL = 10
MONEDA_FALSA = 9

def test_moneda_falsa_random(size_bolsa, posicion_moneda_falsa):
    bolsa_de_monedas = [MONEDA_NORMAL]*(size_bolsa - 1)
    bolsa_de_monedas.insert(posicion_moneda_falsa, MONEDA_FALSA)

    time_dyc = process_time()
    moneda_dyc = ej1.wrapper_detectar_moneda_falsa_dyc(bolsa_de_monedas)
    time_dyc = process_time() - time_dyc

    assert moneda_dyc == MONEDA_FALSA
    print(f"{size_bolsa} monedas (random: posicion {posicion_moneda_falsa})")
    print(f"Moneda falsa (dyc): {moneda_dyc} - Tiempo: {time_dyc:.8f}\n")


def main():

    size_bolsa: int = 10

    try:
        size_bolsa = int(input("Ingrese el tamaño de la bolsa de monedas: "))
    except ValueError:
        print(f"Valor por defecto: {size_bolsa}")

    posicion_moneda_falsa: int = -1
    while (0 > posicion_moneda_falsa) or (posicion_moneda_falsa >= size_bolsa):
        try:
            posicion_moneda_falsa = int(input(f"Ingrese la posición de la moneda falsa (posicion > 0 y posicion < {size_bolsa}): "))
        except ValueError:
            print("Valor no válido")

    test_moneda_falsa_random(size_bolsa, posicion_moneda_falsa)


main()
