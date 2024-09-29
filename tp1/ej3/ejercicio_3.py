

class PossibleValues:
    availables = 0
    values = []

    def __init__(self, valueArray):
        self.values = list(valueArray)
        self.availables = len(self.values)

    def markUsed(self, value):
        self.availables -= 1
        value.used = True

    def markUnused(self, value):
        self.availables += 1
        value.used = False

    def getAvailablesCount(self):
        return self.availables

    def getValues(self):
        return self.values


class PossibleValue:
    def __init__(self, value):
        self.value = value
        self.used = False


class CachedRowColumnDiagonalCalculations:
    def __init__(self, sideSize):
        self.rowTotals = {}
        self.columnTotals = {}
        self.mainDiagonalTotal = 0
        self.secondaryDiagonalTotal = 0
        self.magickConstant = sideSize * (sideSize ** 2 + 1) / 2
        self.sideSize = sideSize
        for i in range(sideSize):
            self.rowTotals[i] = 0
            self.columnTotals[i] = 0

    def addItem(self, row, col, value):
        self.rowTotals[row] += value
        self.columnTotals[col] += value
        if row == col:
            self.mainDiagonalTotal += value
        if row + col == self.sideSize - 1:
            self.secondaryDiagonalTotal += value

    def removeItem(self, row, col, value):
        self.rowTotals[row] -= value
        self.columnTotals[col] -= value
        if row == col:
            self.mainDiagonalTotal -= value
        if row + col == self.sideSize - 1:
            self.secondaryDiagonalTotal -= value

    def getRowTotal(self, row):
        return self.rowTotals[row]

    def getColumnTotal(self, col):
        return self.columnTotals[col]

    def getMainDiagonalTotal(self):
        return self.mainDiagonalTotal

    def getSecondaryDiagonalTotal(self):
        return self.secondaryDiagonalTotal


def compatible(cachedRowColumnDiagonalCalculations, row, col, value):
    magickConstant = cachedRowColumnDiagonalCalculations.magickConstant
    # COMPARA LAS SUMAS DE FILA, COLUMNA Y DIAGONALES
    rowTotal = cachedRowColumnDiagonalCalculations.getRowTotal(row) + value
    # SI LA SUMA DE LA FILA ES MAYOR A LA CONSTANTE MÁGICA, NO ES COMPATIBLE
    if rowTotal > magickConstant:
        return False
    # SI LA SUMA DE LA COLUMNA ES MAYOR A LA CONSTANTE MÁGICA, NO ES COMPATIBLE
    columnTotal = cachedRowColumnDiagonalCalculations.getColumnTotal(col) + value
    if columnTotal > magickConstant:
        return False
    # SI LA SUMA DE LA DIAGONAL PRINCIPAL ES MAYOR A LA CONSTANTE MÁGICA, NO ES COMPATIBLE
    mainDiagonalTotal = cachedRowColumnDiagonalCalculations.getMainDiagonalTotal() + value
    if row == col and mainDiagonalTotal > magickConstant:
        return False
    # SI LA SUMA DE LA DIAGONAL SECUNDARIA ES MAYOR A LA CONSTANTE MÁGICA, NO ES COMPATIBLE
    secondaryDiagonalTotal = cachedRowColumnDiagonalCalculations.getSecondaryDiagonalTotal() + value
    if row + col == cachedRowColumnDiagonalCalculations.sideSize - 1 and secondaryDiagonalTotal > magickConstant:
        return False
    # VALIDA QUE SI ES LA ULTIMA CELDA DE FILA DE LA CONSTANTE MÁGICA
    isLastCellInRow = col == cachedRowColumnDiagonalCalculations.sideSize - 1
    if isLastCellInRow and rowTotal != magickConstant:
        return False
    # VALIDA QUE SI ES LA ULTIMA CELDA DE COLUMNA DE LA CONSTANTE MÁGICA
    isLastCellInColumn = row == cachedRowColumnDiagonalCalculations.sideSize - 1
    if isLastCellInColumn and columnTotal != magickConstant:
        return False
    # VALIDA QUE SI ES LA ULTIMA CELDA DE LA DIAGONAL SECUNDARIA DE LA CONSTANTE MÁGICA
    isLastCellInSecondaryDiagonal = col == 0 and row == cachedRowColumnDiagonalCalculations.sideSize - 1
    if isLastCellInSecondaryDiagonal and secondaryDiagonalTotal != magickConstant:
        return False
    # VALIDA QUE SI ES LA ULTIMA CELDA DE LA DIAGONAL PRINCIPAL DE LA CONSTANTE MÁGICA
    isLastCellInMainDiagonal = row == col and row == cachedRowColumnDiagonalCalculations.sideSize - 1
    if isLastCellInMainDiagonal and mainDiagonalTotal != magickConstant:
        return False
    return True



def fill(square, sideSize, cachedRowColumnDiagonalCalculations, possibleValues, row, col):
    values = possibleValues.getValues()
    for possibleValue in values:

        if len(square) == row and len(square) < sideSize:
            square.append([])

        if not possibleValue.used and compatible(cachedRowColumnDiagonalCalculations, row, col, possibleValue.value):
            cachedRowColumnDiagonalCalculations.addItem(row, col, possibleValue.value)
            if len(square[row]) == col:
                square[row].append(possibleValue.value)
            else:
                square[row][col] = possibleValue.value
    
            possibleValues.markUsed(possibleValue)

            nextRow = 0
            nextCol = 0

            if col == sideSize - 1:
                nextRow = row + 1
                nextCol = 0
            else:
                nextRow = row
                nextCol += col + 1

            if possibleValues.getAvailablesCount() == 0:
                return True

            solutionExists = fill(square, sideSize, cachedRowColumnDiagonalCalculations, possibleValues, nextRow, nextCol)

            if solutionExists:
                return True
            else:
                cachedRowColumnDiagonalCalculations.removeItem(row, col, possibleValue.value)
                possibleValues.markUnused(possibleValue)
                square[row][col] = 0
                if possibleValues.getAvailablesCount() == 0:
                    return False
    return False




def buildMagicSquare(n):
    square = []
    values = []

    for i in range(1, n**2 + 1):
        values.append(PossibleValue(i))

    possibleValues = PossibleValues(reversed(values))

    cachedRowColumnDiagonalCalculations = CachedRowColumnDiagonalCalculations(n)

    sideSize = n

    fill(square, sideSize, cachedRowColumnDiagonalCalculations, possibleValues, 0, 0)

    return square



