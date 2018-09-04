# https://practice.geeksforgeeks.org/problems/gold-mine-problem/0

memoization_dict = {}

def find_max_gold(matrix: list, starting_point=None) -> int:
    if not starting_point:
        memoization_dict.clear()
        max_gold = -1
        for i in range(len(matrix)):
            current_gold = find_max_gold(matrix, (i, 0))
            if current_gold > max_gold:
                max_gold = current_gold
    
    else:
        if starting_point[0] not in range(len(matrix)) or starting_point[1] not in range(len(matrix[0])):
            max_gold = 0
        else:
            if memoization_dict.get(starting_point, None) != None:
                max_gold = memoization_dict[starting_point]
            else:
                max_gold = max( find_max_gold(matrix, (starting_point[0] - 1, starting_point[1] + 1)), 
                                find_max_gold(matrix, (starting_point[0], starting_point[1] + 1)), 
                                find_max_gold(matrix, (starting_point[0] + 1, starting_point[1] + 1)))
                max_gold += matrix[starting_point[0]][starting_point[1]]
                memoization_dict[starting_point] = max_gold
    
    return max_gold


no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    n, m = list(map(int, str(input()).strip().split(' ')))
    elements = list(map(int, str(input()).strip().split(' ')))
    
    row = [0] * m
    matrix = [row[:] for _ in range(n)]
    
    for index, element in enumerate(elements):
        q = index // m
        r = index % m
        matrix[q][r] = element
    
    # print(matrix)

    print(find_max_gold(matrix))