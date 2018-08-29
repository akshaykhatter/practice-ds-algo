last_checked_point = None

def checkbounds(matrix, point):
    global last_checked_point
    if last_checked_point == point:
        return False
    last_checked_point = point
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    x_point = point[0]
    y_point = point[1]

    if x_point in range(rows) and y_point in range(columns):
        return True
    else:
        return False


print(checkbounds([[1,3,5], [3,4,5]], (1, 1)))
print(checkbounds([[1,3,5], [3,4,5]], (1, 1)))