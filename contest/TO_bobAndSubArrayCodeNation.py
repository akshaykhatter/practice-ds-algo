n = int(input())
array = list(map(int, str(input()).strip().split(' ')))

def solution(array):
    result_sum = 0
    
    for start in range(len(array)):
        for end in range(start, len(array)):
            bitwise_or_result = 0
            for i in range(start, end + 1):
                bitwise_or_result = bitwise_or_result | array[i]
            result_sum = result_sum + bitwise_or_result
        
    print(result_sum)

solution(array)


# n = int(input())
# array = list(map(int, str(input()).strip().split(' ')))

# def solution(array):
#     sub_arrays = []
#     result_sum = 0

#     for start in range(len(array)):
#         for end in range(start, len(array)):
#             temp_array = []
#             for i in range(start, end + 1):
#                 temp_array.append(array[i])
#             sub_arrays.append(temp_array)
    
#     result_sum = 0
#     for i in range(len(sub_arrays)):
#         bitwise_or_result = 0
#         for j in range(len(sub_arrays[i])):
#             bitwise_or_result = bitwise_or_result | sub_arrays[i][j]
#         result_sum += bitwise_or_result
        
#     print(result_sum)

# solution(array)