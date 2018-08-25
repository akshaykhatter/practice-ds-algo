matrix = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

aux_matrix = []
no_of_rows = len(matrix)
no_of_columns = len(matrix[0])

# initialise auxillary matrix
for i in range(no_of_rows):
    row = []
    for j in range(no_of_columns):
        row.append(0)
    aux_matrix.append(row)

# prepare auxillary matrix
for i in range(no_of_rows):
    for j in range(no_of_columns):
        if i == 0 or j == 0:
            aux_matrix[i][j] = matrix[i][j]
        elif matrix[i][j] == 0:
            aux_matrix[i][j] = 0
        else:
            min_val = min(aux_matrix[i][j - 1], aux_matrix[i - 1][j - 1], aux_matrix[i - 1][j])
            aux_matrix[i][j] = min_val + 1

# find maximum in auxillary matrix
largest_val = -1
largest_coord = (-1, -1)

for i in range(no_of_rows):
    for j in range(no_of_columns):
        if aux_matrix[i][j] >= largest_val:
            largest_val = aux_matrix[i][j]
            largest_coord = (i, j)

print(f'Largest sq sub matrix hvaing all 1s is from {(i - (largest_val - 1), (j - (largest_val - 1)))} - {largest_coord} and is of size {largest_val}')