from time import process_time
import ejercicio_2 as ej2


# PATH ARCHIVO (Modificar el path en caso de querer probar con un archivo distinto)

PATH_ARCHIVO = "ej2/res/test1.csv"
#PATH_ARCHIVO = "ej2/res/test2.csv"
#PATH_ARCHIVO = "ej2/res/test3.csv"
#PATH_ARCHIVO = "ej2/res/test4.csv"
#PATH_ARCHIVO = "ej2/res/test5.csv"
#PATH_ARCHIVO = "ej2/res/test_no_optimo.csv"



def print_edificios_y_restaurantes_en_grilla(edificios: list, restaurantes: list, tamano_barrio: int, archivo) -> None:
    for i in range(tamano_barrio):
        for j in range(tamano_barrio):
            if (i, j) in edificios and (i, j) not in restaurantes:
                archivo.write("E")
            elif (i, j) in restaurantes:
                archivo.write("R")
            else:
                archivo.write(" ")

            if j != tamano_barrio - 1:
                archivo.write(",")

        archivo.write("\n")


def leer_csv_para_mapear_edificios(archivo: str) -> tuple:
    edificios: list = list()
    tamano_barrio = 0

    with open(archivo, "r") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line):
                if i == 0 and char != "\n" and char != ",":
                    tamano_barrio += 1

                if char == "E":
                    edificios.append((i, int(j/2)))

    return (edificios, tamano_barrio)


def test_ej2() -> None:

    print(f"\n\033[31;1;4mTest con archivo: \033[0m{PATH_ARCHIVO}\n")

    # En caso de querer probar con diferentes archivos, cambiar la constante PATH_ARCHIVO
    datos_entrada = leer_csv_para_mapear_edificios(PATH_ARCHIVO)

    archivo_restaurantes = open("archivo_restaurantes_custom.csv", "w")

    radio_de_cobertura: int = ej2.calcular_radio_de_cobertura(datos_entrada[1])

    start_time: float = process_time()
    restaurantes: list = ej2.construccion_de_restaurantes(datos_entrada[0], datos_entrada[1])
    end_time: float = process_time() - start_time

    print(f"\033[31;1;4mTiempo de ejecución para n = {datos_entrada[1]}:\033[0m {end_time:.8f} segundos")
    print(f"Cantidad de restaurantes: {len(restaurantes)} con cobertura {radio_de_cobertura} (proporcional a N)\nRestaurantes: {restaurantes}\n")
    print_edificios_y_restaurantes_en_grilla(datos_entrada[0], restaurantes, datos_entrada[1], archivo_restaurantes)

    archivo_restaurantes.close()

test_ej2()
