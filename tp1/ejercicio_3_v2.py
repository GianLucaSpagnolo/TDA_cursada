def compatible(magickConstant, sideSize, square, collection, rol, col):
    if len(collection) < sideSize and sum(collection) < magickConstant:
        return True
    if sum(collection) == magickConstant and len(collection) == sideSize:
        return True
    return False

def restorePossibleValues(possibleValues, failedValues):
    for i in reversed(failedValues):
        possibleValues.append(i)
    failedValues.clear()


def fillRow(magickConstant, sideSize, square, possibleValues, failedValues, row, col, value):
    # RETORNA TRUE SI LOGRA LLENAR LA FILA
    if len(square) == row:  # APENDEA FILA SI NO EXISTE
        square.append([])

    square[row].append(value)

    print(square)

    if compatible(magickConstant, sideSize, square, square[row], row, col):
        # RECUPERA VALORES FALLIDOS PARA LAS SIGUIENTES SOLUCIONES PARCIALES
        restorePossibleValues(possibleValues, failedValues)

        if len(square[row]) == sideSize:
            return True

    else:
        # NO ES SOLUCION PARCIAL LA QUITA DE LA FILA
        square[row].pop()
        failedValues.append(value)
        if len(possibleValues) == 0:
            return False

    # ANALIZA SIGUIENTES SOLUCIONES PARCIALES
    newValue = possibleValues.pop()
    return fillRow(magickConstant, sideSize, square, possibleValues, failedValues, row, col + 1, newValue)


def buildMagicSquare(n):
    square = []
    possibleValues = [i for i in range(1, n*n+1)]
    magickConstant = n * (n**2 + 1) / 2
    sideSize = n
    row = 0
    failedValues = []
    
    while len(square) != sideSize:
        value = possibleValues.pop()
        rowFilled = fillRow(magickConstant, sideSize, square, possibleValues, failedValues, row, 0, value)
        if rowFilled:
            row += 1
        else:
            droppedRow = list(square.pop())
            for i in reversed(droppedRow):
                failedValues.insert(1, i)
            restorePossibleValues(possibleValues, failedValues)
        pass





