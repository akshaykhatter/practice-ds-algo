# This is stable implementation. Normal implementation in which we use swapping is unstable

def selection_sort(array: list, is_smaller, ascending=True): # O(n^2)
    if ascending:
        for i in range(len(array)):
            min_value = array[i]
            min_index = -1
            for j in range(i, len(array)):
                if is_smaller(array[j], min_value):
                    min_value = array[j]
                    min_index = j
            if i != min_index:
                for k in range(min_index, i, -1):
                    array[k] = array[k - 1]
                array[i] = min_value
    
    else:
        for i in range(len(array)):
            max_value = array[i]
            max_index = -1
            for j in range(i, len(array)):
                if is_smaller(array[j], max_value, False):
                    max_value = array[j]
                    max_index = j
            if i != max_index:
                for k in range(max_index, i, -1):
                    array[k] = array[k- 1]
                array[i] = max_value


# array = list(map(int, str(input('Enter array of nos: ')).strip().split()))
array = [(4, '0'), (4, 'a'),(2, 'b'),(1, 'c'),(0, 'd'),(10, 'e'),(9, 'f'),(4, 'h'),]

# selection_sort(array, lambda x, y, ascending=True: x < y if ascending else x > y)
selection_sort(array, lambda x, y, ascending=True: x[0] < y[0] if ascending else x[0] > y[0])

print(array)