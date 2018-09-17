n = int(input())
marker_array = [True] * (n + 1)

marker_array[0] = False
marker_array[1] = False

for i in range(2, n + 1):
    if marker_array[i] == False:
        continue
    else:
        j = 2
        result = i * j
        while result <= n:
            marker_array[result] = False
            j += 1
            result = i * j

for i in range(2, n + 1):
    if marker_array[i] == True:
        print(i, end=' ')
