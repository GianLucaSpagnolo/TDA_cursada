from time import time
from ejercicio_3 import buildMagicSquare

N = [3, 4, 5]


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
    start_time = time()
    square = buildMagicSquare(n)
    end_time = time() - start_time
    printSquare(square, n)
    print(f"Tiempo de ejecución para n={n}: {end_time} segundos\n")
