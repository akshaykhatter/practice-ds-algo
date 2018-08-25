def bubble_sort(array: list, is_smaller, ascending=True):
    for i in range(len(array) - 1): # if in an array of n elements, if (n-1) are sorted, then nth element is also in its correct position
        swapped = False
        for j in range(len(array) - 1 - i):
            if is_smaller(array[j], array[j + 1], False) if ascending else is_smaller(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

# array = list(map(int, str(input('Enter array of nos: ')).strip().split()))
array = [(4, '0'), (4, 'a'),(2, 'b'),(1, 'c'),(0, 'd'),(10, 'e'),(9, 'f'),(4, 'h'),]

# bubble_sort(array, lambda x, y, ascending=True: x < y if ascending else x > y, True)
bubble_sort(array, lambda x, y, ascending=True: x[0] < y[0] if ascending else x[0] > y[0])

print(array)