def printSquare(square, sideSize):
    print("---" * sideSize)
    for row in square:
        print(row)


def compatible(magickConstant, sideSize, square, row, col, value):
    # SI LA SUMA DE LA FILA ES MAYOR A LA CONSTANTE MAGICA SE PODA
    if sum(square[row]) + value > magickConstant:
        return False
    # SI LA SUMA DE LA COLUMNA HASTA AHORA ES MAYOR A LA CONSTANTE MAGICA SE PODA
    totalColumna = 0
    if len(square) > 0:
        for i in range(len(square)):
            if len(square[i]) > col:
                totalColumna += square[i][col]
        if totalColumna + value > magickConstant:
            return False
    if row == col and len(square) > 0 and len(square[row]) > 0:
        # La suma de la diagonal principal es mayor a la constante magica
        mainDiagonalTotal = 0
        for i in range(len(square)):
            if(i == len(square[i])):
                break
            mainDiagonalTotal += square[i][i]
        if mainDiagonalTotal + value > magickConstant:
            return False
    printSquare(square, 3)
    # si row + col == n - 1 entonces estamos en la diagonal secundaria
    if row + col == (sideSize - 1):
        secondaryDiagonal = 0
        for i in range(sideSize):
            # si estamos en la posicion actual corta las sumas
            if i == row and col == sideSize - i - 1:
                break
            secondaryDiagonal += square[i][sideSize - i - 1]
        if secondaryDiagonal + value > magickConstant:
            return False
        # La suma de la diagonal secundaria es mayor a la constante magica
    return True



def fill(square, sideSize, magickConstant, possibleValues, row, col):
    for value in possibleValues:
        if len(square) == row:
            square.append([])
        if compatible(magickConstant, sideSize, square, row, col, value):
            # SE CREA COPIA DE LISTA DE VALORES POSIBLES PARA NO MODIFICAR EL ORIGINAL
            # YA QUE SE ESTA ITERANDO Y PUEDE CREAR INCONSISTENCIAS
            possibleValuesOfNext = possibleValues.copy()
            square[row].append(value)
            possibleValuesOfNext.remove(value)

            nextRow = 0
            nextCol = 0

            if len(square[row]) == sideSize:
                nextRow = row + 1
                nextCol = 0
            else:
                nextRow = row
                nextCol += col + 1

            if len(possibleValuesOfNext) == 0:
                return True
            result = fill(square, sideSize, magickConstant, possibleValuesOfNext, nextRow, nextCol)
            if result:
                return True
            else:
                if len(square[row]) > 0:
                    square[row].pop()
                else:
                    square.pop()
                if len(possibleValuesOfNext) == 0:
                    return False
    return False


def buildMagicSquare(n):
    square = []
    possibleValues = [i for i in range(1, n*n+1)]
    possibleValues = list(reversed(possibleValues))
    magickConstant = n * (n**2 + 1) / 2
    sideSize = n
    fill(square, sideSize, magickConstant, possibleValues, 0, 0)
    printSquare(square, sideSize)
