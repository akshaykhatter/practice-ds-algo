import math

x, l, r = list(map(int, str(input()).strip().split(' ')))

def ones_complement(x):
    return x ^ ((1 << x.bit_length()) - 1)

def solve(x, l, r):
    max_xor = -math.inf
    for i in range(r, l-1,-1):
        temp = x ^ i
        if temp > max_xor:
            max_xor = temp
    return max_xor

# print(solve(x, l, r))