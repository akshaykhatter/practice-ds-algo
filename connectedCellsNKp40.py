def countConnectedCells(matrix: list, visitedMatrix: list, noOfRows: int, noOfColumns: int) -> int:
    connectedLengths = []

    for i in range(noOfRows):
        for j in range(noOfColumns):
            if visitedMatrix[i][j] == False and matrix[i][j] == 1:
                connectedLengths.append(connectedRecursive((i, j), matrix, visitedMatrix, noOfRows, noOfColumns))
    
    print('All length\'s is: ', connectedLengths)
    return max(connectedLengths)

def connectedRecursive(point: tuple, matrix: list, visitedMatrix: list, noOfRows: int, noOfColumns: int) -> int:
    pointRow = point[0]
    pointColumn = point[1]

    if visitedMatrix[pointRow][pointColumn]: # this can happen on recursive calls
        return 0
    
    visitedMatrix[pointRow][pointColumn] = True

    sumOfLength = 1

    dirs = [[-1, -1],[-1, 0],[-1, 1],[0, 1],[1, 1],[1, 0],[1, -1],[0, -1]]

    for dir in dirs:
        if checkPoint(pointRow + dir[0], pointColumn + dir[1], noOfRows, noOfColumns, matrix):
            sumOfLength = sumOfLength + connectedRecursive((pointRow + dir[0], pointColumn + dir[1]), matrix, visitedMatrix, noOfRows, noOfColumns)

    return sumOfLength

def checkPoint(i:int, j:int, noOfRows:int, noOfColumns:int, matrix: list):
    if (i in range(noOfRows) and j in range(noOfColumns)) and matrix[i][j] == 1:
        return True
    else:
        return False

matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1]
]

noOfRows = len(matrix)
noOfColumns = len(matrix[0])
visitedMatrix = []

for i in range(noOfRows):
    visitedRow = []
    for j in range(noOfColumns):
        visitedRow.append(False)
    visitedMatrix.append(visitedRow)

print(f'Length of max. connected cells of 1s is {countConnectedCells(matrix, visitedMatrix, noOfRows, noOfColumns)}')
