def elegir_trabajo_primera_semana(seleccionados: list) -> None:

    opt: int = max(trabajos_tranquilos[1], trabajos_estresantes[1])
    if opt == trabajos_tranquilos[1]:
        seleccionados.append("t1")
    else:
        seleccionados.append("e1")

    return opt


def elegir_trabajo_segunda_semana(seleccionados: list) -> None:

    opt_ant: int = elegir_trabajo_primera_semana(seleccionados)
    opt: int = max(opt_ant + trabajos_tranquilos[2], trabajos_estresantes[2])
    if opt == trabajos_tranquilos[2] + opt_ant:
        seleccionados.append("t2")
    else:
        seleccionados.pop()
        seleccionados.append("e2")

    return opt, opt_ant


def elegir_trabajo(opt_ant: int, opt_ante_ant: int, i: int, seleccionados: list) -> None:

    opt = max(opt_ant + trabajos_tranquilos[i], opt_ante_ant + trabajos_estresantes[i])
    if opt == trabajos_tranquilos[i] + opt_ant:
        seleccionados.append(f"t{i}")
    else:
        seleccionados.pop()
        seleccionados.append(f"e{i}")
    opt_ante_ant = opt_ant
    opt_ant = opt

    return opt_ant, opt_ante_ant


def seleccion_de_trabajos(trabajos_estresantes: list, trabajos_tranquilos: list) -> tuple:

    # Agrego un 0 en el indice 0 para "descartarlo" (usaremos a partir del indice 1 para simplificar)
    trabajos_estresantes.insert(0, 0)
    trabajos_tranquilos.insert(0, 0)
    n: int = len(trabajos_estresantes)

    seleccionados: list = list()

    opt_act, opt_ant = elegir_trabajo_segunda_semana(seleccionados)

    for i in range(3, n):
        opt_act, opt_ant = elegir_trabajo(opt_act, opt_ant, i, seleccionados)

    return opt_act, seleccionados


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