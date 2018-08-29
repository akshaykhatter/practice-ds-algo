# https://www.codechef.com/JAN18/problems/KCON

def apply_kadan(count):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, count):
        max_ending_here = max(max_ending_here + arr[i%n], arr[i%n])
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    
    return max_so_far


no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    n, k = tuple(map(int, str(input()).strip().split(' ')))
    arr = list(map(int, str(input()).strip().split(' ')))
    
    # find total sum of single copy of arr
    single_sum = 0
    for i in range(n):
        single_sum = single_sum + arr[i]
    
    # kadan's algo for one copy
    max_so_far_1 = apply_kadan(n)

    # kadan's algo for two copies
    max_so_far_2 = apply_kadan(n*2)

    if k == 1:
        max_sum = max_so_far_1
    elif k == 2:
        max_sum = max_so_far_2
    else:
        if single_sum <= 0:
            max_sum = max_so_far_2
        else:
            max_sum = max_so_far_2 + ((k - 2) * single_sum)
    
    print(max_sum)