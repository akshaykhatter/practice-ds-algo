arr = [0, 0, 0]
arr_limit = [3, 6, 9]

# def increment(array: list) -> int:
#     if array[-1] + 1 == arr_limit[-1]:
#         array[-1] = 0
#         if array[-2] + 1 == arr_limit[-2]:
#             array[-2] = 0
#             if array[-3] + 1 == arr_limit[-3]:
#                 array[-3] = 0
#                 return -1
#             else:
#                 array[-3] += 1
#         else:
#             array[-2] += 1
#     else:
#         array[-1] += 1
    
#     return 0

def increment(array: list, index=-1):
    if (index * -1) > len(array):
        return False
    
    if array[index] + 1 == arr_limit[index]:
        array[index] = 0
        return increment(array, index - 1)
    else:
        array[index] += 1
        return True

while True:
    result = increment(arr)
    print(arr)
    if result == False:
        break
