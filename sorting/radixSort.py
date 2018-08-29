def radix_sort(arr: list):
    # find no of digits in the largest number
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    max_digits = len(str(max_num))

    for i in range(max_digits):
        # initialise count array for counting sort sub routine
        count_arr = [0] * 10
        
        # fill count array
        for j in arr:
            j_str = str(j)
            try:
                pos_val = int(j_str[-1 - i])
            except IndexError:
                pos_val = 0
            count_arr[pos_val] = count_arr[pos_val] + 1
        
        # add previous sum
        for j in range(1, len(count_arr)):
            count_arr[j] = count_arr[j] + count_arr[j - 1]
        
        # initialise result array
        result_arr = [0] * len(arr)

        # fill result array
        # doing it in reverse, to preserve relative order of elements with same current significant digit
        for j_index in range(len(arr) - 1, -1, -1):
            j = arr[j_index]
            j_str = str(j)
            try:
                pos_val = int(j_str[-1 - i])
            except IndexError:
                pos_val = 0
            count_arr[pos_val] = count_arr[pos_val] - 1
            result_arr[count_arr[pos_val]] = j
        
        arr = result_arr

    return arr


print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))