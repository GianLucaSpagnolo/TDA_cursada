
# FUNCION TEMPORAL, REMPLAZAR A FUTURO PARA OPTIMIZAR

def compatible(
    magickConstant,
    sideSize,
    collection
):
    if len(collection) < sideSize and sum(collection) < magickConstant:
        return True
    if sum(collection) == magickConstant and len(collection) == sideSize:
        return True
    return False


def fillMagicSquare(
    magickConstant,
    square,
    possibleValues,
    sideSize,
    rowIndex,
    colIndex,
):
    if len(square) == rowIndex:  # APENDEA FILA SI NO EXISTE
        square.append([])
    if len(possibleValues) == 0 and len(square[rowIndex]) < sideSize:
        return False
    
    # AGREGO UN VALOR
    value = possibleValues.pop()
    square[rowIndex].append(value)

    print(square)
    
    if compatible(magickConstant, sideSize, square[rowIndex]):
        # SOLUCION ENCONTRADA PARA LA FILA
        if len(square[rowIndex]) == sideSize:
            return True

        # SOLUCION PARCIAL ENCONTRADA VALIDA PRUEBO SIGUIENTE VALOR
        existsCompatibleChild = fillMagicSquare(magickConstant, square, possibleValues, sideSize, rowIndex, colIndex + 1)
        
        # NO HAY SOLUCION HIJA COMPATIBLE, BACKTRACKING
        if not existsCompatibleChild:
            square[rowIndex].pop()
            existsCompatibleChild = fillMagicSquare(magickConstant, square, possibleValues, sideSize, rowIndex, colIndex - 1)
            return existsCompatibleChild

        # SE MUEVE A LA SIGUIENTE FILA
        #if colIndex == 0:
            #return fillMagicSquare(magickConstant, square, possibleValues, sideSize, rowIndex + 1, 0)
            
        # SOLUCION ENCONTRADA PARA FILA O PARA CUADRADO
        return True
    else:
        square[rowIndex].pop()
        possibleValues.append(value)
        return False


def buildMagicSquare(n):
    square = []
    sideSize = n
    possibleValues = [i for i in range(1, n*n+1)]
    magickConstant = n * (n**2 + 1) / 2
    fillMagicSquare(magickConstant, square, possibleValues, sideSize, 0, 0)
    return







