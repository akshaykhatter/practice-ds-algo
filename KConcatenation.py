# https://www.codechef.com/JAN18/problems/KCON
### Some cases get timed out

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    n, k = tuple(map(int, str(input()).strip().split(' ')))
    arr = list(map(int, str(input()).strip().split(' ')))
    
    # kadan's algo

    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, n*k):
        max_ending_here = max(max_ending_here + arr[i%n], arr[i%n])
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    print(max_so_far)
