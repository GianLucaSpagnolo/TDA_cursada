def elegir_trabajo_primera_semana(seleccionados: list, trabajos_tranquilos: list, trabajos_estresantes: list) -> None:

    opt_actual: int = max(trabajos_tranquilos[1], trabajos_estresantes[1])
    if opt_actual == trabajos_tranquilos[1]:
        seleccionados.append("t1")
    else:
        seleccionados.append("e1")

    return opt_actual


def elegir_trabajo_segunda_semana(seleccionados: list, trabajos_tranquilos: list, trabajos_estresantes: list) -> None:

    opt_anterior: int = elegir_trabajo_primera_semana(seleccionados, trabajos_tranquilos, trabajos_estresantes)
    opt_actual: int = max(opt_anterior + trabajos_tranquilos[2], trabajos_estresantes[2])
    if opt_actual == trabajos_tranquilos[2] + opt_anterior:
        seleccionados.append("t2")
    else:
        seleccionados.pop()
        seleccionados.append("e2")

    return opt_actual, opt_anterior


def elegir_trabajo(opt_actual: int, opt_anterior: int, i: int, seleccionados: list, trabajos_tranquilos: list, trabajos_estresantes: list) -> None:

    opt = max(opt_actual + trabajos_tranquilos[i], opt_anterior + trabajos_estresantes[i])
    if opt == trabajos_tranquilos[i] + opt_actual:
        seleccionados.append(f"t{i}")
    else:
        seleccionados.append(f"e{i}")

    opt_anterior = opt_actual
    opt_actual = opt

    return opt_actual, opt_anterior


def ajustar_lista_seleccionados(seleccionados: list) -> None:

    i = len(seleccionados) - 1
    while i > 0:
        if "e" in seleccionados[i]:
            del seleccionados[i - 1]
            i -= 1
        i -= 1


def seleccion_de_trabajos(trabajos_estresantes: list, trabajos_tranquilos: list) -> tuple:

    # Agrego un 0 en el indice 0 para "descartarlo" (usaremos a partir del indice 1 para simplificar).
    trabajos_estresantes.insert(0, 0)
    trabajos_tranquilos.insert(0, 0)

    n: int = len(trabajos_estresantes)
    seleccionados: list = list()

    opt_actual, opt_anterior = elegir_trabajo_segunda_semana(seleccionados, trabajos_tranquilos, trabajos_estresantes)

    for i in range(3, n):
        opt_actual, opt_anterior = elegir_trabajo(opt_actual, opt_anterior, i, seleccionados, trabajos_tranquilos, trabajos_estresantes)
    
    ajustar_lista_seleccionados(seleccionados)

    return opt_actual, seleccionados
