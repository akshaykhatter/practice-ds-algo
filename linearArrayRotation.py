array = list(map(int, str(input('enter array elements: ')).rstrip().split(" ")))
rotation = int(input('Rotate by positions: '))

rem_array = []
if rotation > len(array):
    rotation = rotation % len(array)

for r in range(rotation):
    rem_array.append(array[len(array) - rotation + r])

for i in range(len(array) - 1, rotation - 1, -1):
    array[i] = array[i - rotation]

for i in range(rotation):
    array[i] = rem_array[i]

print(array)