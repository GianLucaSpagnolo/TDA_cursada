def elegir_trabajo_primera_semana(opt: list, seleccionados: list) -> None:

    opt[1] = max(trabajos_tranquilos[1], trabajos_estresantes[1])

    if opt[1] == trabajos_tranquilos[1]:
        seleccionados.append("t1")
    else:
        seleccionados.append("e1")


def elegir_trabajo_segunda_semana(opt: list, seleccionados: list) -> None:

    opt[2] = max(opt[1] + trabajos_tranquilos[2], trabajos_estresantes[2])

    if opt[2] == trabajos_tranquilos[2] + opt[1]:
        seleccionados.append("t2")
    else:
        seleccionados.pop()
        seleccionados.append("e2")


def elegir_trabajo(opt: list, i: int, seleccionados: list) -> None:

    opt[i] = max(opt[i - 1] + trabajos_tranquilos[i], opt[i - 2] + trabajos_estresantes[i])

    if opt[i] == trabajos_tranquilos[i] + opt[i - 1]:
        seleccionados.append(f"t{i}")
    else:
        seleccionados.pop()
        seleccionados.append(f"e{i}")


def seleccion_de_trabajos(trabajos_estresantes: list, trabajos_tranquilos: list) -> tuple:

    # Agrego un 0 en el indice 0 para "descartarlo" (usaremos a partir del indice 1 para simplificar)
    trabajos_estresantes.insert(0, 0)
    trabajos_tranquilos.insert(0, 0)

    n: int = len(trabajos_estresantes)

    opt: list = [0] * n

    seleccionados: list = list()

    elegir_trabajo_primera_semana(opt, seleccionados)
    elegir_trabajo_segunda_semana(opt, seleccionados)

    for i in range(3, n):
        elegir_trabajo(opt, i, seleccionados)

    return opt[n - 1], seleccionados


print("\nEJEMPLO 1")
trabajos_estresantes: list = [8, 6, 20, 2, 9]
trabajos_tranquilos: list = [8, 6, 4, 5, 2]

beneficio, trabajos_a_realizar = seleccion_de_trabajos(trabajos_estresantes, trabajos_tranquilos)
print(f"\n\tSe ha obtenido un beneficio total de {beneficio}.")
print(f"\nLos trabajos a realizar son: {trabajos_a_realizar}.")


print("\n\n")


print("EJEMPLO 2")
trabajos_estresantes: list = [8, 8, 15, 7, 12, 17, 9, 29]
trabajos_tranquilos: list = [7, 9, 5, 15, 10, 12, 11, 14]

beneficio, trabajos_a_realizar = seleccion_de_trabajos(trabajos_estresantes, trabajos_tranquilos)
print(f"\n\tSe ha obtenido un beneficio total de {beneficio}.")
print(f"\nLos trabajos a realizar son: {trabajos_a_realizar}.\n")