def merge_sort(arr: list, start, end):
    if (end - start) < 2:
        return
    
    mid_index = (end - start) // 2 + start
    merge_sort(arr, start, mid_index)
    merge_sort(arr, mid_index + 1, end)
    merge(arr, start, mid_index, mid_index + 1, end)


def merge(arr, start_1, end_1, start_2, end_2):
    result = []
    i = start_1
    j = start_2

    while i <= end_1 and j <= end_2:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1
    
    if i < end_1:
        result.extend(arr[i:end_1 + 1])
    else:
        result.extend(arr[j:end_2 + 1])
    
    # replacing two sublists with their merged variant
    arr[start_1: end_2 + 1] = result


arr = [5, 4, -3, 2, 0, 10, -2, -1]
merge_sort(arr, 0, len(arr) - 1)
print(arr)

# time: O(n * log(n)) - all 3 types
# space: O(n)
# stable