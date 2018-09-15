import math
from heapq import heappush, heappop

def mining(k: int, mines: list):
    unresolved_mines = []
    move_to_mines = []
    move_min_cost = [] # min heap

    for i in range(len(mines)):
        unresolved_mines.append(i)
        move_to_mines.append(i)

        min_cost = math.inf
        min_cost_mine = -1
        for j in range(len(mines)):
            if i != j:
                current_cost = (abs(mines[i][0] - mines[j][0]) * mines[i][1])
                if current_cost < min_cost:
                    min_cost = current_cost
                    min_cost_mine = j
        heappush(move_min_cost, (min_cost, min_cost_mine, i))
    
    return recursive_mining(k, 1, move_min_cost[:], unresolved_mines[:], move_to_mines[:])

def recursive_mining(k: int, l: int, move_min_cost: list, unresolved_mines: list, move_to_mines: list):
    cost, goto_mine, i = heappop(move_min_cost)
    unresolved_mines.remove(i)

    if l > k: # k mines have already been selected
        return 
    else:
        result_not_shift_current = recursive_mining(k, l + 1, move_min_cost[:], unresolved_mines[:], move_to_mines[:])
        result_shift_current = recursive_mining(k, l, move_min_cost[:], unresolved_mines[:], (move_to_mines[:]).remove(i))
        return max(result_not_shift_current, result_shift_current)






n, k = list(map(int, str(input()).strip().split(' ')))

mines = []

for _ in range(n):
    mines.append(list(map(int, input().rstrip().split())))

# result = mining(k, mines)
mining(k, mines)

# print(result)