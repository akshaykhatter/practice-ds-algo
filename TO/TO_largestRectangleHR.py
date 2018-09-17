import math

def largestRectangle(h):
    length = len(h)
    max_area = -math.inf

    for start in range(length):
        for end in range(start, length):
            no_of_buildings = end - start + 1
            min_height = math.inf
            for i in range(start, end + 1):
                if h[i] < min_height:
                    min_height = h[i]
            area = no_of_buildings * min_height
            if area > max_area:
                max_area = area
    return max_area

# tried_cases = set()

# def largestRectangle(h):
#     mid = len(h) // 2 + 1
#     return largest_rectangle(h, mid, mid)

# def get_area(h, start, end):
#     no_of_buildings = end - start + 1
#     min_height = math.inf

#     for i in range(start, end + 1):
#         if h[i] < min_height:
#             min_height = h[i]
    
#     area = no_of_buildings * min_height
#     return area

# def largest_rectangle(h, start_index, end_index, current_area = None):
#     global tried_cases
    
#     length = len(h)
#     if current_area is None:
#         current_area = h[start_index] # * 1
    
#     if start_index > 0:
#         if (start_index - 1, end_index) not in tried_cases:
#             print(f'({start_index - 1}, {end_index})')
#             area = largest_rectangle(h, start_index - 1, end_index, get_area(h, start_index - 1, end_index))
#             if area > current_area:
#                 current_area = area
#             tried_cases.add((start_index - 1, end_index))
    
#     if end_index < (length - 1):
#         if (start_index, end_index + 1) not in tried_cases:
#             print(f'({start_index}, {end_index + 1})')
#             area = largest_rectangle(h, start_index, end_index + 1, get_area(h, start_index, end_index + 1))
#             if area > current_area:
#                 current_area = area
#             tried_cases.add((start_index, end_index + 1))

#     print(current_area)
#     return current_area


n = int(input())
h = list(map(int, str(input()).strip().split(' ')))
result = largestRectangle(h)
# print('---')
print(result)