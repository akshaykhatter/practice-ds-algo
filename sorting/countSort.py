def count_sort(arr: list, max_num=None, min_num=None):
    # find min and max num if not present
    if not max_num or not min_num:
        max_num = min_num = arr[0]
        for i in arr:
            if i < min_num:
                min_num = i
            elif i > max_num:
                max_num = i
    
    # initialise count array
    range_min_max = max_num - min_num + 1
    count_arr = [0] * range_min_max
    # fill count array
    for i in arr:
        count_arr[i - min_num] = count_arr[i - min_num] + 1
    # add previous sum
    for j in range(1, len(count_arr)):
        count_arr[j] = count_arr[j] + count_arr[j - 1]
    
    # initialise result array
    result_arr = [0] * len(arr)
    # fill result array
    for i in arr:
        count_arr[i - min_num] = count_arr[i - min_num] - 1
        index = count_arr[i - min_num]
        result_arr[index] = i
    
    return result_arr

print(count_sort([1, 4, 1, 2, 7, 5, 2]))

# time: O(n + k)
# space: O(n + k)
# stable
# not online    
