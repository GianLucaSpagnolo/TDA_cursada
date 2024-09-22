def compatible(magickConstant, square, row, col, value):
    if sum(square[row]) + value > magickConstant:
        return False
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
            print(square)
            possibleValuesOfNext.pop(0)
            if len(square[row]) == sideSize:
                row += 1
                col = 0
            else:
                col += 1
            result = fill(square, sideSize, magickConstant, possibleValuesOfNext, row, col)
            if result:
                return True
            else:
                square[row].pop()
    return False


def buildMagicSquare(n):
    square = []
    possibleValues = [i for i in range(1, n*n+1)]
    possibleValues = list(reversed(possibleValues))
    magickConstant = n * (n**2 + 1) / 2
    sideSize = n
    fill(square, sideSize, magickConstant, possibleValues, 0, 0)
