from time import time
from random import randint

import ejercicio_1 as ej1

CANTIDADES_DE_MONEDAS = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 10000000]
MONEDA_FALSA = 9

def test_moneda_falsa_random(cantidad):
    bolsa_de_monedas = [10]*(cantidad - 1)
    random_pos = randint(0, cantidad - 1)
    bolsa_de_monedas.insert(random_pos, MONEDA_FALSA)
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_dyc(bolsa_de_monedas)
    time_rec = time() - time_rec

    assert moneda_lineal == MONEDA_FALSA and moneda_rec == MONEDA_FALSA
    print(f"{cantidad} monedas (random: posicion {random_pos})")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal:.8f}")
    print(f"Moneda falsa    (dyc): {moneda_rec}. Tiempo: {time_rec:.8f}\n")

def test_modena_falsa_inicio(cantidad):
    bolsa_de_monedas = [MONEDA_FALSA] + [10]*(cantidad - 1)
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_dyc(bolsa_de_monedas)
    time_rec = time() - time_rec

    assert moneda_lineal == MONEDA_FALSA and moneda_rec == MONEDA_FALSA
    print(f"{cantidad} monedas (caso inicio)")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal:.8f}")
    print(f"Moneda falsa    (dyc): {moneda_rec}. Tiempo: {time_rec:.8f}\n")

def test_moneda_falsa_mitad(cantidad):
    bolsa_de_monedas = [10]*(cantidad//2) + [MONEDA_FALSA] + [10]*(cantidad//2)
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_dyc(bolsa_de_monedas)
    time_rec = time() - time_rec

    assert moneda_lineal == MONEDA_FALSA and moneda_rec == MONEDA_FALSA
    print(f"{cantidad} monedas (caso mitad)")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal:.8f}")
    print(f"Moneda falsa    (dyc): {moneda_rec}. Tiempo: {time_rec:.8f}\n")

def test_modena_falsa_final(cantidad):
    bolsa_de_monedas = [10]*(cantidad - 1) + [MONEDA_FALSA]
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_dyc(bolsa_de_monedas)
    time_rec = time() - time_rec

    assert moneda_lineal == MONEDA_FALSA and moneda_rec == MONEDA_FALSA
    print(f"{cantidad} monedas (caso final)")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal:.8f}")
    print(f"Moneda falsa    (dyc): {moneda_rec}. Tiempo: {time_rec:.8f}\n")


# Testeo de casos de prueba
for cantidad in CANTIDADES_DE_MONEDAS:
    print(f"\033[31;1;4mTesteando con {cantidad} monedas\033[0m")
    test_moneda_falsa_random(cantidad)
    test_modena_falsa_inicio(cantidad)
    test_moneda_falsa_mitad(cantidad)
    test_modena_falsa_final(cantidad)
