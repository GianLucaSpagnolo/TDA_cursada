from time import time
from random import randint

# Versión lineal O(n) en su peor caso

def detectar_moneda_falsa_lineal(bolsa_de_monedas, largo_inicio, largo_fin):
    if largo_fin == 0:
        return bolsa_de_monedas[largo_inicio]
    
    if bolsa_de_monedas[largo_inicio] < bolsa_de_monedas[largo_inicio + 1]:
        return bolsa_de_monedas[largo_inicio]

    for i in range(1, largo_fin+1):
        if bolsa_de_monedas[i] < bolsa_de_monedas[i-1]:
            return bolsa_de_monedas[i]

def wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas):
    return detectar_moneda_falsa_lineal(bolsa_de_monedas, 0, len(bolsa_de_monedas)-1)

# Versión recursiva
# Complejidad temporal (teorema maestro):
#


def detectar_moneda_falsa_rec(bolsa_de_monedas, largo_inicio, largo_fin):
    if (largo_fin == 0) | (largo_fin - largo_inicio == 1):
        return bolsa_de_monedas[largo_inicio]
    
    mitad = (largo_inicio + largo_fin) // 2
    if sum(bolsa_de_monedas[largo_inicio:mitad]) < sum(bolsa_de_monedas[mitad:largo_fin]):
        return detectar_moneda_falsa_rec(bolsa_de_monedas, largo_inicio, mitad)
    else:
        return detectar_moneda_falsa_rec(bolsa_de_monedas, mitad, largo_fin)

def wrapper_detectar_moneda_falsa_rec(bolsa_de_monedas):
    return detectar_moneda_falsa_rec(bolsa_de_monedas, 0, len(bolsa_de_monedas)-1)
    

# Casos de prueba:

MONEDAS_1 = [10]
time_lineal_1 = time()
moneda_1_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDAS_1)
time_lineal_1 = time() - time_lineal_1
time_1 = time()
moneda_1 = wrapper_detectar_moneda_falsa_rec(MONEDAS_1)
time_1 = time() - time_1
print("\n1 moneda")
print(f"Moneda falsa (lineal): {moneda_1_lineal}. Tiempo: {time_lineal_1}")
print(f"Moneda falsa (rec): {moneda_1}. Tiempo: {time_1}")

MONEDAS_10 = [10, 10, 10, 10, 10, 10, 9, 10, 10, 10]
time_lineal_10 = time()
moneda_10_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDAS_10)
time_lineal_10 = time() - time_lineal_10
time_10 = time()
moneda_10 = wrapper_detectar_moneda_falsa_rec(MONEDAS_10)
time_10 = time() - time_10
print("\n10 monedas")
print(f"Moneda falsa (lineal): {moneda_10_lineal}. Tiempo: {time_lineal_10}")
print(f"Moneda falsa (rec): {moneda_10}. Tiempo: {time_10}")

MONEDA_10_INICIO = [9, 10, 10, 10, 10, 10, 10, 10, 10, 10]
time_lineal_10_inicio = time()
moneda_10_inicio_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDA_10_INICIO)
time_lineal_10_inicio = time() - time_lineal_10_inicio
time_10_inicio = time()
moneda_10_inicio = wrapper_detectar_moneda_falsa_rec(MONEDA_10_INICIO)
time_10_inicio = time() - time_10_inicio
print("\n10 monedas (caso inicio)")
print(f"Moneda falsa (lineal): {moneda_10_inicio_lineal}. Tiempo: {time_lineal_10_inicio}")
print(f"Moneda falsa (rec): {moneda_10_inicio}. Tiempo: {time_10_inicio}")

MONEDAS_10_FINAL = [10, 10, 10, 10, 10, 10, 10, 10, 10, 9]
time_lineal_10_final = time()
moneda_10_final_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDAS_10_FINAL)
time_lineal_10_final = time() - time_lineal_10_final
time_10_final = time()
moneda_10_final = wrapper_detectar_moneda_falsa_rec(MONEDAS_10_FINAL)
time_10_final = time() - time_10_final
print("\n10 monedas (caso final)")
print(f"Moneda falsa (lineal): {moneda_10_final_lineal}. Tiempo: {time_lineal_10_final}")
print(f"Moneda falsa (rec): {moneda_10_final}. Tiempo: {time_10_final}")

MONEDAS_100000 = [10]*99999
MONEDAS_100000.insert(randint(0, 99999), 9)
time_lineal_100000 = time()
moneda_100000_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDAS_100000)
time_lineal_100000 = time() - time_lineal_100000
time_100000 = time()
moneda_100000 = wrapper_detectar_moneda_falsa_rec(MONEDAS_100000)
time_100000 = time() - time_100000
print("\n100000 monedas")
print(f"Moneda falsa (lineal): {moneda_100000_lineal}. Tiempo: {time_lineal_100000}")
print(f"Moneda falsa (rec): {moneda_100000}. Tiempo: {time_100000}")

MONEDAS_100000_INICIO = [9]
MONEDAS_100000_INICIO.extend([10]*99999)
time_lineal_100000_inicio = time()
moneda_100000_inicio_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDAS_100000_INICIO)
time_lineal_100000_inicio = time() - time_lineal_100000_inicio
time_100000_inicio = time()
moneda_100000_inicio = wrapper_detectar_moneda_falsa_rec(MONEDAS_100000_INICIO)
time_100000_inicio = time() - time_100000_inicio
print("\n100000 monedas (caso inicio)")
print(f"Moneda falsa (lineal): {moneda_100000_inicio_lineal}. Tiempo: {time_lineal_100000_inicio}")
print(f"Moneda falsa (rec): {moneda_100000_inicio}. Tiempo: {time_100000_inicio}")

MONEDAS_100000_FINAL = [10]*99999
MONEDAS_100000_FINAL.append(9)
time_lineal_100000_final = time()
moneda_100000_final_lineal = wrapper_detectar_moneda_falsa_lineal(MONEDAS_100000_FINAL)
time_lineal_100000_final = time() - time_lineal_100000_final
time_100000_final = time()
moneda_100000_final = wrapper_detectar_moneda_falsa_rec(MONEDAS_100000_FINAL)
time_100000_final = time() - time_100000_final
print("\n100000 monedas (caso final)")
print(f"Moneda falsa (lineal): {moneda_100000_final_lineal}. Tiempo: {time_lineal_100000_final}")
print(f"Moneda falsa (rec): {moneda_100000_final}. Tiempo: {time_100000_final}")
