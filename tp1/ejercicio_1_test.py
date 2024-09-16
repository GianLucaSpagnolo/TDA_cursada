from time import time
from random import randint

import lib.ejercicio_1 as ej1

CANTIDADES_DE_MONEDAS = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 10000000]

def test_moneda_falsa_random(cantidad):
    bolsa_de_monedas = [10]*(cantidad - 1)
    bolsa_de_monedas.insert(randint(0, cantidad - 1), 9)
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_rec(bolsa_de_monedas)
    time_rec = time() - time_rec
    assert moneda_lineal == moneda_rec
    print(f"\n{cantidad} monedas (random)")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal}")
    print(f"Moneda falsa    (rec): {moneda_rec}. Tiempo: {time_rec}")

def test_modena_falsa_inicio(cantidad):
    bolsa_de_monedas = [9] + [10]*(cantidad - 1)
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_rec(bolsa_de_monedas)
    time_rec = time() - time_rec
    assert moneda_lineal == moneda_rec
    print(f"\n{cantidad} monedas (caso inicio)")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal}")
    print(f"Moneda falsa    (rec): {moneda_rec}. Tiempo: {time_rec}")

def test_modena_falsa_final(cantidad):
    bolsa_de_monedas = [10]*(cantidad - 1) + [9]
    time_lineal = time()
    moneda_lineal = ej1.wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas)
    time_lineal = time() - time_lineal
    time_rec = time()
    moneda_rec = ej1.wrapper_detectar_moneda_falsa_rec(bolsa_de_monedas)
    time_rec = time() - time_rec
    assert moneda_lineal == moneda_rec
    print(f"\n{cantidad} monedas (caso final)")
    print(f"Moneda falsa (lineal): {moneda_lineal}. Tiempo: {time_lineal}")
    print(f"Moneda falsa    (rec): {moneda_rec}. Tiempo: {time_rec}")


# Testeo de casos de prueba
print("Testeo de casos de prueba:")
for cantidad in CANTIDADES_DE_MONEDAS:
    test_moneda_falsa_random(cantidad)
    test_modena_falsa_inicio(cantidad)
    test_modena_falsa_final(cantidad)
