from time import process_time
import ejercicio_1 as ej1
import ejercicio_1_sin_lista_de_opt as ej1_no_opt


# PATH ARCHIVO (para testear con diferentes sets de datos). En caso de querer agregar un testeo propio, cambiar la constante PATH_ARCHIVO

#PATH_ARCHIVO = "ej1/res/test1.csv"
#PATH_ARCHIVO = "ej1/res/test2.csv"
#PATH_ARCHIVO = "ej1/res/test3.csv"
#PATH_ARCHIVO = "ej1/res/test4.csv"
#PATH_ARCHIVO = "ej1/res/test5.csv"
PATH_ARCHIVO = "ej1/res/test_brian.csv"


def leer_csv_para_identificar_trabajos(archivo: str) -> tuple:
    cantidad_trabajos = 0
    trabajos_tranquilos = list()
    trabajos_estresantes = list()

    with open(archivo, "r") as file:
        for line in file:
            line = line.strip().split(",")
            trabajos_tranquilos.append(int(line[1]))
            trabajos_estresantes.append(int(line[2]))
            cantidad_trabajos += 1

    return cantidad_trabajos, trabajos_tranquilos, trabajos_estresantes


def test_ej2() -> None:
    print(f"\n\033[31;1;4mTest con archivo:\033[0m {PATH_ARCHIVO}")


    print("\n\033[31;1;4mPlanificacion de trabajos (con lista de optimos):\033[0m\n")

    cantidad_trabajos, trabajos_tranquilos, trabajos_estresantes = leer_csv_para_identificar_trabajos(PATH_ARCHIVO)

    start_time: float = process_time()
    beneficio, trabajos_a_realizar = ej1.seleccion_de_trabajos(trabajos_estresantes, trabajos_tranquilos)
    end_time: float = process_time() - start_time

    print(f"Tiempo de ejecución para \033[31;1mn = {cantidad_trabajos}\033[0m: {end_time:.8f} segundos")
    print(f"Se ha obtenido un beneficio total de {beneficio}.")
    print(f"Los trabajos a realizar son: {trabajos_a_realizar}.")


    print("\n\033[31;1;4mPlanificacion de trabajos (sin lista de optimos):\033[0m\n")

    cantidad_trabajos_no_opt, trabajos_tranquilos_no_opt, trabajos_estresantes_no_opt = leer_csv_para_identificar_trabajos(PATH_ARCHIVO)

    start_time: float = process_time()
    beneficio_no_opt, trabajos_a_realizar_no_opt = ej1_no_opt.seleccion_de_trabajos(trabajos_estresantes_no_opt, trabajos_tranquilos_no_opt)
    end_time: float = process_time() - start_time

    print(f"Tiempo de ejecución para \033[31;1mn = {cantidad_trabajos_no_opt}\033[0m: {end_time:.8f} segundos")
    print(f"Se ha obtenido un beneficio total de {beneficio_no_opt}.")
    print(f"Los trabajos a realizar son: {trabajos_a_realizar_no_opt}.")


test_ej2()
