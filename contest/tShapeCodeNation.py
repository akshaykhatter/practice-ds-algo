import math

def solve(grid):
    t_vertical_dict = {}
    t_vertical_points = {}
    t_horizontal_dict = {}
    t_horizontal_points = {}

    result = 'No'
    has_3_vertical = False
    has_3_horizontal = False
    max_vertical = -math.inf
    min_vertical = math.inf
    max_horizontal = -math.inf
    min_horizontal = math.inf

    # check three points lie in a line vertically and horizontally
    for index in range(len(grid)):
        x, y = grid[index]

        if y > max_vertical:
            max_vertical = y
        elif y < min_vertical:
            min_vertical = y
        if x > max_horizontal:
            max_horizontal = x
        elif x < min_horizontal:
            min_horizontal = x

        if y in t_vertical_dict.keys():
            t_vertical_dict[y] = t_vertical_dict[y] + 1
            t_vertical_points[y].add((x, y))
        else:
            t_vertical_dict[y] = 1
            t_vertical_points[y] = set()
            t_vertical_points[y].add((x, y))

        if x in t_horizontal_dict.keys():
            t_horizontal_dict[x] = t_horizontal_dict[x] + 1
            t_horizontal_points[x].add((x, y))
        else:
            t_horizontal_dict[x] = 1
            t_horizontal_points[x] = set()
            t_horizontal_points[x].add((x, y))
    
    for i in t_vertical_dict.keys():
        if t_vertical_dict[i] == 3:
            t_vertical_common = i
            has_3_vertical = True
            break
    for j in t_horizontal_dict.keys():
        if t_horizontal_dict[j] == 3:
            t_horizontal_common = j
            has_3_horizontal = True
            break

    if has_3_horizontal and has_3_vertical:
        common_set = t_vertical_points[t_vertical_common].intersection(t_horizontal_points[t_horizontal_common])
        common_point = common_set.pop()

        if common_point[1] == min_vertical or common_point[1] == max_vertical:
            result = 'Yes'
        elif common_point[0] == min_horizontal or common_point[0] == max_horizontal:
            result = 'Yes'
    
    return result


no_of_test_cases = int(input())
points = []

for _ in range(no_of_test_cases):
    
    for i in range(5):
        point = list(map(int, str(input()).strip().split(' ')))
        points.append(point)
    result = solve(points)
    print(result)