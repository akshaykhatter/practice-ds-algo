array = list(map(int, str(input('Enter array: ')).strip().split()))

max_so_far = max_ending_here = array[0]
start = end = 0
m = n = 0

for i in range(1, len(array)):

    if max_ending_here + array[i] >= array[i]:
        max_ending_here = max_ending_here + array[i]
        n = i
    else:
        max_ending_here = array[i]
        m = n = i

    if max_ending_here > max_so_far:
        max_so_far = max_ending_here
        start = m
        end = n

print(f'Max subarray sum is {max_so_far}, with starting index {start} and ending index {end}')