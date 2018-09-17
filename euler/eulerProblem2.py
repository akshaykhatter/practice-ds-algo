# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    n = int(input())

    a = 1
    b = 2
    even_sum = 0

    while b < n:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b

    print(even_sum)