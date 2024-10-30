from time import process_time
import ejercicio_1 as ej1
import ejercicio_1_sin_lista_de_opt as ej1_no_opt


# PATH ARCHIVO (para testear con diferentes sets de datos). 
# En caso de querer agregar un testeo propio, cambiar la constante PATH_ARCHIVO (siempre debe haber 1 constante PATH_ARCHIVO sin comentar)

PATH_ARCHIVO = "ej1/res/trabajos_10.csv"
#PATH_ARCHIVO = "ej1/res/trabajos_50.csv"
#PATH_ARCHIVO = "ej1/res/trabajos_100.csv"
#PATH_ARCHIVO = "ej1/res/trabajos_500.csv"
#PATH_ARCHIVO = "ej1/res/trabajos_1000.csv"
#PATH_ARCHIVO = "ej1/res/trabajos_5000.csv"
#PATH_ARCHIVO = "ej1/res/trabajos_10000.csv"
#PATH_ARCHIVO = "ej1/res/test_brian.csv"




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

def verificacion_de_planificacion(trabajos: list) -> bool:
    for i in range(1, len(trabajos)):
        numero_trabajo: int = int(trabajos[i][1:])
        numero_trabajo_anterior: int = int(trabajos[i - 1][1:])
        if trabajos[i][0] == "e" and numero_trabajo - numero_trabajo_anterior == 1:
            return False
    return True


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

    assert(beneficio == beneficio_no_opt)
    assert(trabajos_a_realizar == trabajos_a_realizar_no_opt)

    if (verificacion_de_planificacion(trabajos_a_realizar)):
        print("\n\033[32;1mLa planificación de trabajos es correcta.\033[0m\n")
    else:
        print("\n\033[31;1mLa planificación de trabajos es incorrecta.\033[0m\n")

test_ej2()
