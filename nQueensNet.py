# https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/

def printBoard(n: int, board: list):
    for i in range(n):
        print('[ ', end="")
        for j in range(n):
            print(board[i][j], end=" ")
        print(']')

def checkIfSafe(n: int, board: list, row: int, col: int):
    # Since we are filling queens in left to right fashion, we
    # only need to check the left portion
    
    # checking horizontal left
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # checking top left diagonal
    for (i, j) in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # checking bottom left diagonal
    for (i, j) in zip(range(row+1, n, 1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def nQueensRecursive(n: int, board: list, col: int):
    if col >= n:
        return True
    else:
        for i in range(n):
            if checkIfSafe(n, board, i, col):
                board[i][col] = 1

                if nQueensRecursive(n, board, col + 1): # == True
                    return True

                board[i][col] = 0

        return False

def nQueens():
    n = int(input("Enter 'n' in nQueens: "))
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)
    
    if nQueensRecursive(n, board, 0):
        printBoard(n, board)
    else:
        print('A solution cannot be found')
    

nQueens()