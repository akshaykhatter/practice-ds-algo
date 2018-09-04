# Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. 
# This algorithm avoids large shifts as in case of insertion sort, 
# If the smaller value is to the far right and has to be moved to the far left.

def shell_sort(arr: list):
    h = len(arr) // 2
    while h != 0:
        # start from the second element of the sub list, and slide window of gap(h)
        for i in range(h, len(arr)):
            current = arr[i]
            j = i
            while (j - h) >= 0 and arr[j - h] > current:
                arr[j] = arr[j - h]
                j = j - h
            arr[j] = current
        h = h // 2
    return arr


print(shell_sort([12, 10, 0, 14, 20, 21, -1, -5]))
print(shell_sort([170, 45, 75, 90, 802, 24, 2, 66]))

# time: O(n^2)
# space: O(1)
# online: no
# stable: yes