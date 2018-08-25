memoization_dict = {}

# def get_normalised_coords(coord1: tuple, coord2: tuple, quadrant: int):
#     if quadrant == 1:
#         length = coord1[0] - coord2[0] + 1
#         coordA = (coord1[0] - length + 1, coord1[1])
#         coordB = (coord2[0] + length - 1, coord2[1])
#     elif quadrant == 2:
#         coordA = coord2
#         coordB = coord1
#     elif quadrant == 3:
#         length = coord2[0] - coord1[0] + 1
#         coordA = (coord2[0] - length + 1, coord2[1])
#         coordB = (coord1[0] + length - 1, coord1[1])
#     else:
#         coordA = coord1
#         coordB = coord2

#     return (coordA, coordB)


def check_fill(matrix: list, coordA: tuple, coordB: tuple):
    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])

    if coordA[0] not in range(no_of_rows) or \
    coordB[0] not in range(no_of_rows) or \
    coordA[1] not in range(no_of_columns) or \
    coordB[1] not in range(no_of_columns):
        return False

    if coordA == coordB:
        if matrix[coordA[0]][coordA[1]] == 1:
            memoization_dict[(coordA, coordA)] = True
            return True
        else:
            memoization_dict[(coordA, coordA)] = False
            return False
    else:
        if memoization_dict[(coordA, (coordB[0] - 1, coordB[1] - 1))]: # this will always exists by the way we are calling check_fill, hence we don;t use get()
            
            for i in range(coordA[1], coordB[1] + 1):
                if matrix[coordB[0]][i] == 0:
                    memoization_dict[(coordA, coordB)] = False
                    return False
            for i in range(coordB[0] - 1, coordA[0] - 1, -1):
                if matrix[i][coordB[1]] == 0:
                    memoization_dict[(coordA, coordB)] = False
                    return False
            
            memoization_dict[(coordA, coordB)] = True
            return True
        else:
            memoization_dict[(coordA, coordB)] = False
            return False
    
    

def get_max_fill(matrix: list, pivot: tuple):
    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])

    row_space = no_of_rows - pivot[0]
    col_space = no_of_columns - pivot[1]

    limit = min(row_space, col_space)

    max_fill = 0

    for i in range(limit):
        if check_fill(matrix, pivot, (pivot[0] + i, pivot[1] + i)):
                max_fill = i + 1

    return max_fill

matrix = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

result_coord = (-1, -1)
result_size = -1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        size = get_max_fill(matrix, (i, j))
        if size >= result_size:
            result_size = size
            result_coord = (i, j)

print(memoization_dict)
print(len(memoization_dict))
# in case of same size, gives the last (bottom right) submatrix
print(f'The largest sub-square matrix is at {result_coord} of size {result_size}')
