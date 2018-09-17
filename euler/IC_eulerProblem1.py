# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
# Two test cases are failing

no_of_test_cases = int(input())

# for _ in range(no_of_test_cases):
#     n = int(input())
#     multiple_sum = 0
#     for i in range(2, n):
#         if (i % 3 == 0) or (i % 5 == 0):
#             multiple_sum += i
#     print(multiple_sum)

for _ in range(no_of_test_cases):
    n = int(input())
    sum_3 = sum_5 = sum_15 = 0

    if n >= 3:
        n_3 = n // 3 if (n // 3 != n / 3) else n // 3 - 1
        sum_3 = (n_3 / 2) * (2 * 3 + (n_3 - 1) * 3)    
    if n >= 5:
        n_5 = n // 5 if (n // 5 != n / 5) else n // 5 - 1
        sum_5 = (n_5 / 2) * (2 * 5 + (n_5 - 1) * 5)
    if n >= 15:
        n_15 = n // 15 if (n // 15 != n / 15) else n // 15 - 1
        sum_15 = (n_15 / 2) * (2 * 15 + (n_15 - 1) * 15)

    result = int(sum_3 + sum_5 - sum_15)
    print(result)