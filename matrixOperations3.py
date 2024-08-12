

def matrixTranspose(a):
    """
    Returns the transpose of matrix a.
    
    Parameters:
    a (list of list of int/float): The input matrix.
    
    Returns:
    list of list of int/float: The transposed matrix.
    """
    transposedMatrix = [[] for _ in range(len(a[0]))]  # Create an empty nested list for the transposed matrix
    for r in range(len(a)):  # Iterate over rows of the original matrix
        for c in range(len(a[r])):  # Iterate over columns of the original matrix
            transposedMatrix[c].append(a[r][c])  # Append the element to the transposed matrix at the transposed position
    return transposedMatrix


def matrixMultiplication(a, b):
    """
    Multiplies two matrices a and b.
    
    Parameters:
    a (list of list of int/float): The first matrix.
    b (list of list of int/float): The second matrix.
    
    Returns:
    list of list of int/float: The result of matrix multiplication.
    """
    multipliedMatrix = [[] for _ in range(len(a))]  # Create an empty nested list for the resulting matrix
    
    if len(a[0]) == len(b):  # Check if matrices are compatible for multiplication
        for c in range(len(b[0])):  # Iterate over columns of matrix b
            for r in range(len(a)):  # Iterate over rows of matrix a
                sumOf = 0  # Initialize the sum for the current element of the resulting matrix
                for j in range(len(a[0])):  # Iterate over elements to calculate the dot product
                    elementProduct = a[r][j] * b[j][c]  # Multiply corresponding elements
                    sumOf += elementProduct  # Add the product to the sum
                multipliedMatrix[r].append(sumOf)  # Append the sum to the resulting matrix
    else:
        print("Due to the dimensions of your matrices multiplication cannot be performed.\nFor matrix multiplication one requires that matrix 'a' has dimension m x n and matrix 'b' has dimensions n x p (where one has rows x columns).")

    return multipliedMatrix


def isSquareMatrix(a):
    """
    Checks if the matrix a is a square matrix.
    
    Parameters:
    a (list of list of int/float): The input matrix.
    
    Returns:
    list of list of int/float: The same matrix if it is square.
    
    Raises:
    ValueError: If the matrix is not square.
    """
    if len(a) != len(a[0]):  # Check if the number of rows is equal to the number of columns
        raise ValueError("Matrix is not square and cannot be inverted and a determinant cannot be found")
    else:
        return a  # Return the matrix if it is square


def findSubMatrix(a, row, colum):
    """
    Returns the submatrix of a by removing the specified row and column.
    
    Parameters:
    a (list of list of int/float): The input matrix.
    row (int): The row to be removed.
    colum (int): The column to be removed.
    
    Returns:
    list of list of int/float: The resulting submatrix.
    """
    minorMatrix = []
    for r in range(len(a)):  # Iterate over rows of the matrix
        if r != row:  # Skip the specified row
            minorMatrix.append([a[r][c] for c in range(len(a[r])) if c != colum])  # Append the row without the specified column
    return minorMatrix


def recursiveDeterminant(a):
    """
    Recursively calculates the determinant of matrix a.
    
    Parameters:
    a (list of list of int/float): The input matrix.
    
    Returns:
    int/float: The determinant of the matrix.
    """
    if len(a) == 1:  # Base case for 1x1 matrix
        return a[0][0]
    elif len(a) == 2:  # Base case for 2x2 matrix
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        det = 0  # Initialize determinant
        for c in range(len(a)):  # Iterate over columns of the first row
            det += ((-1) ** c) * a[0][c] * recursiveDeterminant(findSubMatrix(a, 0, c))  # Add the cofactor times the minor's determinant
        return det


def findMatrixDeterminant(a):
    """
    Finds the determinant of a square matrix a.
    
    Parameters:
    a (list of list of int/float): The input matrix.
    
    Returns:
    int/float: The determinant of the matrix.
    """
    b = isSquareMatrix(a)  # Check if the matrix is square
    return recursiveDeterminant(b)  # Calculate the determinant recursively


def findInverseMatrix(a):
    """
    Finds the inverse of matrix a.
    
    Parameters:
    a (list of list of int/float): The input matrix.
    
    Returns:
    list of list of int/float: The inverse of the matrix.
    
    Raises:
    ValueError: If the matrix is singular and cannot be inverted.
    """
    b = isSquareMatrix(a)  # Check if the matrix is square

    determinant = findMatrixDeterminant(b)  # Find the determinant
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted")  # Raise an error if the matrix is singular
    
    aInverse = [[] for _ in range(len(b))]  # Create an empty nested list for the inverse matrix

    for r in range(len(b)):  # Iterate over rows of the matrix
        for c in range(len(b[r])):  # Iterate over columns of the matrix
            minor = findSubMatrix(b, r, c)  # Find the submatrix
            element = ((-1) ** (r + c)) * recursiveDeterminant(minor) / determinant  # Calculate the cofactor divided by the determinant
            aInverse[r].append(element)  # Append the element to the inverse matrix

    aInverse = matrixTranspose(aInverse)  # Transpose the cofactor matrix to get the adjugate matrix
    return aInverse


