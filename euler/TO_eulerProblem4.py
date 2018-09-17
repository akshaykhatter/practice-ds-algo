# https://www.hackerrank.com/contests/projecteuler/challenges/euler004
# 2 test cases getting timed out

import sys
import math

# pairs = []

def check_pallindrome(n):
    str_n = str(n)
    length = len(str_n)
    for i in range(length // 2):
        j = (length - 1) - i
        if str_n[i] != str_n[j]:
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_pallindrome = -math.inf

    for i in range(999, 99, -1):
        for j in range(min(n // i, 999), 99, -1):
            if i % 10 == 0 or j % 10 == 0:
                continue
            product = i * j
            if product > max_pallindrome and check_pallindrome(product):
                max_pallindrome = product
                # pairs.append((i, j))

    print(max_pallindrome)
    # print(pairs[-1])