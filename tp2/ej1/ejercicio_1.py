def elegir_trabajo_primera_semana(ben: list, seleccionados: list) -> None:

    ben[0] = max(trabajos_tranquilos[0], trabajos_estresantes[0])
    if ben[0] == trabajos_tranquilos[0]:
        seleccionados.append("t1")
    else:
        seleccionados.append("e1")


def elegir_trabajo_segunda_semana(ben: list, seleccionados: list) -> None:

    ben[1] = max(ben[0] + trabajos_tranquilos[1], trabajos_estresantes[1])
    if ben[1] == trabajos_tranquilos[1] + ben[0]:
        seleccionados.append("t2")
    else:
        seleccionados.append("e2")
        del seleccionados[0]


def elegir_trabajo_a_realizar(ben: list, i: int, seleccionados: list) -> None:

    ben[i] = max(ben[i - 1] + trabajos_tranquilos[i], ben[i - 2] + trabajos_estresantes[i])
    if ben[i] == trabajos_tranquilos[i] + ben[i - 1]:
        seleccionados.append(f"t{i + 1}")
    else:
        seleccionados.pop()
        seleccionados.append(f"e{i + 1}")


def seleccion_de_trabajos(trabajos_estresantes: list, trabajos_tranquilos: list) -> tuple:

    n = len(trabajos_estresantes)

    ben: list = [0] * n
    seleccionados: list = list()

    elegir_trabajo_primera_semana(ben, seleccionados)
    elegir_trabajo_segunda_semana(ben, seleccionados)

    for i in range(2, n):
        elegir_trabajo_a_realizar(ben, i, seleccionados)

    return ben[n - 1], seleccionados


print("\nEJEMPLO 1")
trabajos_estresantes: list = [8, 6, 20, 2, 9]
trabajos_tranquilos: list = [8, 6, 4, 5, 2]

beneficio, trabajos_a_realizar = seleccion_de_trabajos(trabajos_estresantes, trabajos_tranquilos)
print(f"\n\tSe ha obtenido un beneficio total de {beneficio}.")
print(f"\nLos trabajos a realizar son: {trabajos_a_realizar}.")


print("\n\n")


print("EJEMPLO 2")
trabajos_estresantes: list = [8, 8, 15, 7, 12, 17, 9, 29]
trabajos_tranquilos: list = [7, 9, 6, 15, 10, 12, 11, 14]

beneficio, trabajos_a_realizar = seleccion_de_trabajos(trabajos_estresantes, trabajos_tranquilos)
print(f"\n\tSe ha obtenido un beneficio total de {beneficio}.")
print(f"\nLos trabajos a realizar son: {trabajos_a_realizar}.\n")