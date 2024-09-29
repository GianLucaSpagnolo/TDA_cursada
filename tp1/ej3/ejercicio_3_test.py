from time import process_time
from ejercicio_3 import buildMagicSquare

N = [3, 4] # A partir de N = 5, la complejidad temporal es muy alta y el algoritmo no termina en un tiempo razonable


def printSquare(square, sideSize):
    print("------" * sideSize + "-")
    for row in square:
        print("|", end="")
        for cell in row:
            str = cell.__str__()
            if cell < 10:
                str = " " + str
            if cell < 100:
                str = " " + str
            print("", str, end=" |")
        print("")
    print("------" * sideSize + "-")


for n in N:
    print(f"Cuadrado magico de N x N con N={n}")
    start_time = process_time()
    square = buildMagicSquare(n)
    end_time = process_time() - start_time
    printSquare(square, n)
    print(f"Tiempo de ejecución para n={n}: {end_time} segundos\n")
