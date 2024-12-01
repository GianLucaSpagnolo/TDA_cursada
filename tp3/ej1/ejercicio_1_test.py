from time import process_time
import ejercicio_1 as ej1

# PATH ARCHIVO (para testear con diferentes grafos). 
# En caso de querer cambiar el archivo a testear, cambiar la constante PATH_ARCHIVO (siempre debe haber 1 constante PATH_ARCHIVO sin comentar)
# Se puede disponer de un archivo .csv con un grafo personalizado el cual debe ser ubicado en el directorio ej1/res

PATH_ARCHIVO = "ej1/res/grafo_1.csv"



def leer_csv_para_crear_grafo(archivo: str) -> dict:

    cantidad_vertices = 0
    cantidad_aristas = 0
    grafo = dict()

    with open(archivo, "r") as file:
        for line in file:
            line = line.strip().split(",")
            aristas = list()

            vertice = int(line[0])
            aristas_str = line[1:]

            for arista in aristas_str:
                aristas.append(int(arista))
            
            grafo[vertice] = aristas

            cantidad_vertices += 1
            cantidad_aristas += len(aristas)

    cantidad_aristas //= 2 # Grafo no dirigido, no se cuentan las aristas dos veces
    return cantidad_vertices, cantidad_aristas, grafo


def test_ej1() -> None:

    print("\033[31;1;4mProblema de 3-Coloreo\033[0m")
    print(f"\n\033[31;1;4mTest con archivo:\033[0m {PATH_ARCHIVO}\n")

    cantidad_vertices, cantidad_aristas, grafo = leer_csv_para_crear_grafo(PATH_ARCHIVO)

    # Se espera, al menos, 2/3 aristas satisfechas
    aristas_satisfechas_esperadas = ej1.obtener_aristas_satisfechas_minimas(cantidad_aristas)

    start_time: float = process_time()
    asignacion_obtenida, aristas_satisfechas, cantidad_iteraciones = ej1.problema_3_coloreo_aleatorio(grafo, aristas_satisfechas_esperadas)
    end_time: float = process_time() - start_time

    print(f"Tiempo de ejecución: {end_time:.8f} segundos")
    print(f"Grafo obtenido (con colores de cada vertice): {asignacion_obtenida}")
    print(f"\nAristas Totales: {cantidad_aristas}\nAristas Satisfechas: {aristas_satisfechas}\nCantidad de Iteraciones: {cantidad_iteraciones}")

test_ej1()
