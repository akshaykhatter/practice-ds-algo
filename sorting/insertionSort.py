def insertion_sort(array: list, is_smaller, ascending=True): # Best case: when every element is already at its correct pos O(n) , ohteriwse O(n^2)
    for i in range(1, len(array)):
        current_element = array[i]
        j = i
        while ( is_smaller(array[j - 1], current_element, False) if ascending else is_smaller(array[j - 1], current_element) ) and j > 0:
            array[j] = array[j - 1]
            j = j - 1
        array[j] = current_element

# array = list(map(int, str(input('Enter array of nos: ')).strip().split()))
array = [(4, '0'), (4, 'a'),(2, 'b'),(1, 'c'),(0, 'd'),(10, 'e'),(9, 'f'),(4, 'h'),]

# insertion_sort(array, lambda x, y, ascending=True: x < y if ascending else x > y)
insertion_sort(array, lambda x, y, ascending=True: x[0] < y[0] if ascending else x[0] > y[0])

print(array)

# can use binary search to find correct position to insert in sorted sub array, 
# then its called binaryinsertion sort but the time complexity remains same, since time taken to shift elements is linear

# time: O(n^2)
# space: O(1)
# stable: yes
# online: yes
