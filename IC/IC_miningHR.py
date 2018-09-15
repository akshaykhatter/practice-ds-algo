# https://www.hackerrank.com/challenges/mining/problem

import sys

def mining(k, mines):
    
    result_dict = {}
    closest_mines = {}

    # Add all mines in these two sets
    goto_set = set()
    unresolved_set = set()
    for i in range(len(mines)):
        goto_set.add(i)
        unresolved_set.add(i)
    
    # main loop
    while len(unresolved_set) != 0:
        
        # fill closest mines dict
        closest_mines.clear()
        for i in unresolved_set:    

            closest_mine = None
            closest_cost = sys.maxsize
            
            for j in goto_set:
                if i != j:
                    if (abs(mines[i][0] - mines[j][0]) * mines[i][1]) < closest_cost:
                        closest_cost = (abs(mines[i][0] - mines[j][0]) * mines[i][1])
                        closest_mine = j
            
            closest_mines[i] = (closest_mine, closest_cost)


        # find smallest cost in closest mines dict
        smallest_closest_mine_cost = [None, sys.maxsize]
        to_shift_mine = None 
        
        for key, val in closest_mines.items():
            if val[1] < smallest_closest_mine_cost[1]:
                smallest_closest_mine_cost = list(val)
                to_shift_mine = key
        
        # add to result
        result_dict[to_shift_mine] = smallest_closest_mine_cost
        result_dict[smallest_closest_mine_cost[0]] = [-1, 0]
        # remove to_shift and destination mine from unresolved set
        unresolved_set.remove(to_shift_mine)
        if smallest_closest_mine_cost[0] in unresolved_set:
            unresolved_set.remove(smallest_closest_mine_cost[0])
        # remove to_shift mine from goto_set
        goto_set.remove(to_shift_mine)

        # print(f'result dict: {result_dict}')

    result = 0
    for i in result_dict.values():
        result += i[1]

    return result


n, k = list(map(int, str(input()).strip().split(' ')))

mines = []

for _ in range(n):
    mines.append(list(map(int, input().rstrip().split())))

result = mining(k, mines)

print(result)
