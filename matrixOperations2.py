
a = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
b = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
c = [[7, 2], [4, 3]]
detmat = [[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]]







def findCofactorMatrix(a, row, colum):

    minorMatrix = [[] for row in range(len(a) - 1)]

    for c in range(len(a[0])):
        for r in range(row, len(a)):
            if c != colum:
                minorMatrix[r - 1].append(a[r][c])
    
    return minorMatrix






def findCofactorMatrix2(a, row, colum):

    minorMatrix = [[] for row in range(len(a) - 1)]

    if row != 0:
        for c in range(len(a[0])):
            for r in range(row, len(a)):
                if c != colum:
                    minorMatrix[r - 1].append(a[r][c])

    else:
        for c in range(len(a[0])):
            for r in range(0, len(a) - 1):
                if c != colum:
                    minorMatrix[r - 1].append(a[r][c])
    
    return minorMatrix






def recursiveDeterminant(a):

    det = 0
    if len(a) == 1:
        return a[0][0]
        
    elif len(a) == 2:
        det += a[0][0] * a[1][1] - a[0][1] * a[1][0] 
    
    else:
        sign = 1
        for c in range(len(a[0])):
            det += sign * a[0][c] * recursiveDeterminant(findCofactorMatrix(a, 1, c))
            sign *= -1

    return det















def findSubMatrix(a, row, colum):

    minorMatrix = [[] for row in range(len(a) - 1)]
    addto = 0
    for r in range(len(a)):
        print("row =" + str(r))
        for c in range(len(a[r])):
            print("col =" + str(c))
            if r != row or c != colum:
                minorMatrix[addto].append(a[r][c])
            else:
                pass
        addto += 1
    return minorMatrix








def findMatrixDeterminant(a):

    b = isSquareMatrix(a)

    if b == None:
        pass
    
    else:
        det = recursiveDeterminant(b)
        return det
    







def findInverseMatrix(a):

    aInverse = [[] for row in range(len(a))]

    sign = 1
    for r in range(a):
        for c in range(a[r]):
            element = sign * findCofactorMatrix(a, r, c)
            aInverse[r].append(element)
            sign *= -1




    return aInverse
