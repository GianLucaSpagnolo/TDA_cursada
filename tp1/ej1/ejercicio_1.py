def detectar_moneda_falsa_lineal(bolsa_de_monedas, largo_inicio, largo_fin):
    if largo_fin == 0:
        return bolsa_de_monedas[largo_inicio]
    
    if bolsa_de_monedas[largo_inicio] < bolsa_de_monedas[largo_inicio + 1]:
        return bolsa_de_monedas[largo_inicio]

    for i in range(1, largo_fin+1):
        if bolsa_de_monedas[i] < bolsa_de_monedas[i-1]:
            return bolsa_de_monedas[i]

def wrapper_detectar_moneda_falsa_lineal(bolsa_de_monedas):
    """
    Versión lineal: O(n) en su peor caso
    """
    return detectar_moneda_falsa_lineal(bolsa_de_monedas, 0, len(bolsa_de_monedas)-1)


def detectar_monedas_falsa_dyc(monedas, start_index, end_index):
    # Caso base: O(1)
    if end_index - start_index <= 1:
        if monedas[start_index] < monedas[end_index]:
            return monedas[start_index]
        else:
            return monedas[end_index]

    # Caso recursivo: O(n log n)
    mid_index = start_index + (end_index - start_index) // 2

    moneda_izq = detectar_monedas_falsa_dyc(monedas, start_index, mid_index)
    if moneda_izq < monedas[mid_index + 1]:
        return moneda_izq
    
    moneda_der = detectar_monedas_falsa_dyc(monedas, mid_index + 1, end_index)
    return moneda_der

def wrapper_detectar_moneda_falsa_dyc(monedas):
    """
    Versión Division y Conquista:

    Complejidad temporal (teorema maestro):
    T(n) = 2 T(n/2) + O(n^1)

    a = 2, b = 2, c = 1

    log_b(a) = log_2(2) = 1
    
    log_b(a) = c => O(n^c log_b(n)) = O(n^1 log_2(n))

    Complejidad temporal O(n log n)
    """
    return detectar_monedas_falsa_dyc(monedas, 0, len(monedas) - 1)
