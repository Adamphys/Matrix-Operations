
a = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
b = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
c = [[7, 2], [4, 3]]
detmat = [[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]]
inversemat = [[0, 0, -1, 2], [0, 1, 0, 0], [9, 0, 0, 0], [0, 0, 0, 1]]







def matrixTranspose(a):

    transposedMatrix = [[] for colums in range(len(a[0]))]                                                                                                                             #Creates empty nested array where if one inputs a n x m matrix, m nest arrays are created
    for r in range(len(a)):                                                                                                                                                       #Cycles through the rows of array a
        for c in range(len(a[r])):                                                                                                                                                #Cycles through the colums of array a
            transposedMatrix[c].append(a[r][c])                                                                                                                                   #Appends the element of the jth (column) element of row i to the jth row of aTranspose
            
    return transposedMatrix








def matrixMultiplication(a, b):                                                                                                                                                     

    multipliedMatrix = [[] for row in range(len(a))]                                                                                                                            #Creates empty nested arrays, the product of two matrices a and b with dimensions m x p and p x n (rows x columns) respectively results in a m x n matrix, the number of rows we for the procuct matrix = the number of rows in matrix a                                                                                                                                 
    
    if len(a[0]) == len(b):                                                                                                                                                     #Checks that the matrixs are compatible for multiplications, where the number of colums in matrix == number of rows in matrix b
        for c in range(len(b[0])):                                                                                                                                             #Loops through the columns of matrix b
            for r in range(len(a)):                                                                                                                                            #Loops through the rows of matrix a  
                sumOf = 0                                                                                                                                                       #Stores of the sum for the output matrix of the relevent products of rows and colums forming the elements of the final output matrix
                for j in range(len(a[0])):                                                                                                                                      #Loops through the relevent of columns of row ia in a and the revevent rows of column ib in b
                    elementProduct = a[r][j] * b[j][c]                                                                                                                        #Multiplies relevent elements together from matrix a and b
                    sumOf += elementProduct                                                                                                                                     #Stores each individual multiplication, if c = ab then cij = aik bkj where we sum over repeated indices
                multipliedMatrix[r].append(sumOf)                                                                                                                              #The resulting element is appened to its relevent row, the loops using ia and ib are ordered such that append works to store the output result, the matrix is produced top to bottom and then left to right.
    
    else:
        print("Due to the dimensions of your matrices multiplication cannot be performed.\nFor matrix multiplication one requires that matrix \'a\' has dimension m x n and matrix \'b\' has dimensions n x p (where one has rows x columns).")

    return multipliedMatrix








def isSquareMatrix(a):

    if len(a) != len(a[0]):                                                                                                                                                 #Checks if the number of rows is the same as the number of columns, ie a square matrix
        raise ValueError("Matrix is not square and cannot be inverted and a determinant cannot be found")                                                        #If the matrix is not square it prints to screen this
    else:
        return a                                                                                                                                                            #Returns the matrix a if it is square








def findCofactorMatrix(a, row, colum):

    minorMatrix = [[] for row in range(len(a) - 1)]

    for c in range(len(a[0])):
        for r in range(row, len(a)):
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
            det += (-1**c) * a[0][c] * recursiveDeterminant(findCofactorMatrix(a, 1, c))

    return det








def findSubMatrix(a, row, colum):

    minorMatrix = [[] for row in range(len(a) - 1)]
    addto = 0

    for r in range(len(a)):

        if r == row:
            continue

        else:
            for c in range(len(a[r])):
                if c != colum:
                    minorMatrix[addto].append(a[r][c])
                else: pass

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

    b = isSquareMatrix(a)

    determinant = findMatrixDeterminant(b)
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    
    aInverse = [[] for row in range(len(b))]

    for r in range(len(b)):
        for c in range(len(b[r])):
            minor = findSubMatrix(b, r, c)
            element = (1/ determinant) * ((-1) ** (r + c)) * recursiveDeterminant(minor)
            aInverse[r].append(element)

    aInverse = matrixTranspose(aInverse)
    return aInverse

print(findInverseMatrix(inversemat))
