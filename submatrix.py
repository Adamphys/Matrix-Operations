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
                    print("minor matrix =")
                    print(minorMatrix)

                else: pass

        addto += 1


    return minorMatrix



detmat = [[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]]

print(findSubMatrix(detmat, 0, 0))