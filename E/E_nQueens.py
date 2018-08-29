# https://pastebin.com/j0BsGCS4

def fillDangerCells(n:int, dangerCells: dict, allocatedSpaces: list):
    if len(allocatedSpaces) == 0:
        return
    else:
        currentQueen = allocatedSpaces[-1]
        i = currentQueen[0]
        j = currentQueen[1]

        # vertical and horizontal
        for m in range(n):
            # vertical
            if dangerCells.get((m, j), None) is None:
                dangerCells[(m, j)] = {(i, j)}
            else:
                dangerCells[(m, j)].add((i, j))
            
            # horizontal
            if dangerCells.get((i, m), None) is None:
                dangerCells[(i, m)] = {(i, j)}
            else:
                dangerCells[(i, m)].add((i, j))
        
        # top left
        u, v = i, j
        while u in range(n) and v in range(n):
            if dangerCells.get((u, v), None) is None:
                dangerCells[(u, v)] = {(i, j)}
            else:
                dangerCells[(u, v)].add((i, j))

            u, v = u - 1, v - 1

        # top right
        u, v = i, j
        while u in range(n) and v in range(n):
            if dangerCells.get((u, v), None) is None:
                dangerCells[(u, v)] = {(i, j)}
            else:
                dangerCells[(u, v)].add((i, j))

            u, v = u - 1, v + 1
        
        # bottom left
        u, v = i, j
        while u in range(n) and v in range(n):
            if dangerCells.get((u, v), None) is None:
                dangerCells[(u, v)] = {(i, j)}
            else:
                dangerCells[(u, v)].add((i, j))

            u, v = u + 1, v - 1

        # bottom right
        u, v = i, j
        while u in range(n) and v in range(n):
            if dangerCells.get((u, v), None) is None:
                dangerCells[(u, v)] = {(i, j)}
            else:
                dangerCells[(u, v)].add((i, j))

            u, v = u + 1, v + 1

def clearDangerCells(current: tuple, dangerCells: dict):
    for (_, value) in dangerCells.items():
        if current in value:
            value.remove(current)

def checkSafety(location: tuple, dangerCells: dict):
    if dangerCells.get(location, None) is None:
        return True
    elif len(dangerCells.get(location, None)) == 0:
        return True
    else:
        return False

def nQueens(n:int):
    dangerCells = {}
    allocatedSpaces = []

    queensLeft = n
    lastQueenRemovedPosition = None

    while queensLeft != 0:
        if len(allocatedSpaces) == 0:
            startRow = 0
        else:
            lastQueenAt = allocatedSpaces[-1]
            startRow = lastQueenAt[0] + 1
        
        queenInserted = False
        
        for col in range(n):
            if (startRow, col) != lastQueenRemovedPosition and checkSafety((startRow, col), dangerCells):
                allocatedSpaces.append((startRow, col))
                fillDangerCells(n, dangerCells, allocatedSpaces)
                lastQueenRemovedPosition = None
                queensLeft = queensLeft - 1

                queenInserted = True
                break
        
        if not queenInserted:
            removedQueen = allocatedSpaces.pop()
            clearDangerCells(removedQueen, dangerCells)
            lastQueenRemovedPosition = removedQueen
            queensLeft = queensLeft + 1
    
    print('Process completed')
    
nQueens(4)