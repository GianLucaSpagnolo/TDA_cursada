def printSquare(square, sideSize):
    print("---" * sideSize)
    for row in square:
        print(row)


def compatible(magickConstant, square, row, col, value):
    # SI LA SUMA DE LA FILA ES MAYOR A LA CONSTANTE MAGICA SE PODA
    if sum(square[row]) + value > magickConstant:
        return False
    # SI LA SUMA DE LA COLUMNA HASTA AHORA ES MAYOR A LA CONSTANTE MAGICA SE PODA
    totalColumna = 0
    #for i in range(len(square) - 1):
    #    totalColumna += square[i][col]
    #if totalColumna + value > magickConstant:
    #    return False
    return True


def fill(square, sideSize, magickConstant, possibleValues, row, col):
    for value in possibleValues:
        if len(square) == row:
            square.append([])
        if compatible(magickConstant, square, row, col, value):
            # SE CREA COPIA DE LISTA DE VALORES POSIBLES PARA NO MODIFICAR EL ORIGINAL
            # YA QUE SE ESTA ITERANDO Y PUEDE CREAR INCONSISTENCIAS
            possibleValuesOfNext = possibleValues.copy()
            square[row].append(value)
            possibleValuesOfNext.remove(value)
            printSquare(square, sideSize)
            if len(square[row]) == sideSize:
                row += 1
                col = 0
            else:
                col += 1

            if len(possibleValuesOfNext) == 0:
                return True
            result = fill(square, sideSize, magickConstant, possibleValuesOfNext, row, col)
            if result:
                return True
            else:
                if len(square[row]) > 0:
                    square[row].pop()
                possibleValuesOfNext.insert(0, value)
    return False


def buildMagicSquare(n):
    square = []
    possibleValues = [i for i in range(1, n*n+1)]
    possibleValues = list(reversed(possibleValues))
    magickConstant = n * (n**2 + 1) / 2
    sideSize = n
    fill(square, sideSize, magickConstant, possibleValues, 0, 0)
