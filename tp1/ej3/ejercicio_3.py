import os


def printSquare(square, sideSize):
    os.system('clear')
    print("---" * sideSize)
    for row in square:
        print(row)
    print("---" * sideSize)


def compatible(magickConstant, sideSize, square, row, col, value):
    # Si la suma de la fila es mayor a la constante magica se poda
    rowTotal = sum(square[row]) + value
    if rowTotal > magickConstant:
        return False
    # La suma de la fila es menor a la constante magica
    if rowTotal < magickConstant and col == sideSize - 1:
        return False


    # Si la suma de la columna hasta ahora es mayor
    # a la constante magica se poda
    totalColumna = 0
    if len(square) > 0:
        for i in range(len(square)):
            if len(square[i]) > col:
                totalColumna += square[i][col]
        # La suma de la columna es mayor a la constante magica
        if totalColumna + value > magickConstant:
            return False
        # La suma de la columna es menor a la constante magica
        if totalColumna + value < magickConstant and row == sideSize - 1:
            return False


    # La suma de la diagonal principal es mayor a la constante magica
    if row == col and len(square) > 0 and len(square[row]) > 0:
        mainDiagonalTotal = 0
        for i in range(len(square)):
            if i == len(square[i]):
                break
            mainDiagonalTotal += square[i][i]
        # La suma de la diagonal principal es mayor a la constante magica
        if mainDiagonalTotal + value > magickConstant:
            return False
        # La suma de la diagonal principal es menor a la constante magica
        if mainDiagonalTotal + value < magickConstant and row == sideSize - 1 and col == sideSize - 1:
            return False

    # si row + col == n - 1 entonces estamos en la diagonal secundaria
    if row + col == (sideSize - 1):
        secondaryDiagonal = 0
        for i in range(sideSize):
            # si estamos en la posicion actual corta las sumas
            if i == row and col == sideSize - i - 1:
                break
            secondaryDiagonal += square[i][sideSize - i - 1]
        # La suma de la diagonal secundaria es mayor a la constante magica
        if secondaryDiagonal + value > magickConstant:
            return False
        # Termino pero la suma es menor a la constante magica
        if secondaryDiagonal + value < magickConstant and row == sideSize - 1 and col == 0:
            return False
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

            printSquare(square, sideSize)

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
