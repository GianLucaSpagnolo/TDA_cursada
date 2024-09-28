from time import process_time
from random import randint, seed

import ejercicio_1 as ej1

CANTIDADES_DE_MONEDAS = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
MONEDA_FALSA = 9

def test_moneda_falsa_random(cantidad):
    bolsa_de_monedas = [10]*(cantidad - 1)
    random_pos = randint(0, cantidad - 1)
    bolsa_de_monedas.insert(random_pos, MONEDA_FALSA)

    time_dyc = process_time()
    moneda_dyc = ej1.wrapper_detectar_moneda_falsa_dyc(bolsa_de_monedas)
    time_dyc = process_time() - time_dyc

    assert moneda_dyc == MONEDA_FALSA
    print(f"{cantidad} monedas (random: posicion {random_pos})")
    print(f"Moneda falsa (dyc): {moneda_dyc} - Tiempo: {time_dyc:.8f}\n")


def main():
    seed(5000)
    # Testeo de casos de prueba
    for cantidad in CANTIDADES_DE_MONEDAS:
        test_moneda_falsa_random(cantidad)


main()
