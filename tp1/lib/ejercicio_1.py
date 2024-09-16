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


# Versión Division y Conquista
# Complejidad temporal (teorema maestro):
#
def detectar_monedas_falsa(monedas, start_index, end_index):
    if start_index >= end_index:
        return monedas[start_index]

    mid_index = start_index + (end_index - start_index) // 2

    mid = monedas[start_index:mid_index+1]
    expected_weight = len(mid) * max(monedas[0], monedas[1])

    if sum(mid) < expected_weight:
        return detectar_monedas_falsa(monedas, start_index, mid_index)
    else:
        return detectar_monedas_falsa(monedas, mid_index + 1, end_index)
 
def wrapper_detectar_moneda_falsa_rec(monedas):
    return detectar_monedas_falsa(monedas, 0, len(monedas) - 1)
