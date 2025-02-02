def elegir_trabajo_primera_semana(opt: list, seleccionados: list, trabajos_tranquilos: list, trabajos_estresantes: list) -> None:

    opt[1] = max(trabajos_tranquilos[1], trabajos_estresantes[1])
    if opt[1] == trabajos_tranquilos[1]:
        seleccionados.append("t1")
    else:
        seleccionados.append("e1")


def elegir_trabajo_segunda_semana(opt: list, seleccionados: list, trabajos_tranquilos: list, trabajos_estresantes: list) -> None:

    opt[2] = max(opt[1] + trabajos_tranquilos[2], trabajos_estresantes[2])
    if opt[2] == trabajos_tranquilos[2] + opt[1]:
        seleccionados.append("t2")
    else:
        seleccionados.append("e2")


def elegir_trabajo(opt: list, i: int, seleccionados: list, trabajos_tranquilos: list, trabajos_estresantes: list) -> None:

    opt[i] = max(opt[i - 1] + trabajos_tranquilos[i], opt[i - 2] + trabajos_estresantes[i])
    if opt[i] == trabajos_tranquilos[i] + opt[i - 1]:
        seleccionados.append(f"t{i}")
    else:
        seleccionados.append(f"e{i}")


def ajustar_lista_seleccionados(seleccionados: list) -> list:

    aux: list = []
    i: int = len(seleccionados) - 1

    # Recorro la lista de fin a principio, si encuentro un trabajo estresante, ignoro el inmediatamente anterior y continuo iterando.
    while i > 0:
        aux.append(seleccionados[i])
        if "e" == seleccionados[i][0]:
            i -= 1
        i -= 1
    aux.reverse()

    return aux


def seleccion_de_trabajos(trabajos_tranquilos: list, trabajos_estresantes: list) -> tuple:

    # Agrego un 0 en el indice 0 para "descartarlo" (usaremos a partir del indice 1 para simplificar)
    trabajos_tranquilos.insert(0, 0)
    trabajos_estresantes.insert(0, 0)

    n: int = len(trabajos_tranquilos)
    opt: list = [0] * n
    seleccionados: list = [0]

    elegir_trabajo_primera_semana(opt, seleccionados, trabajos_tranquilos, trabajos_estresantes)
    elegir_trabajo_segunda_semana(opt, seleccionados, trabajos_tranquilos, trabajos_estresantes)

    for i in range(3, n):
        elegir_trabajo(opt, i, seleccionados, trabajos_tranquilos, trabajos_estresantes)
    seleccionados = ajustar_lista_seleccionados(seleccionados)

    return opt[n - 1], seleccionados
