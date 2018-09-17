# https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
# one test case failing

# def sieve_primes(n):
#     marker_array = [True] * (n + 1)
#     marker_array[0] = False
#     marker_array[1] = False

#     for i in range(2, n + 1):
#         if marker_array[i] == False:
#             continue
#         else:
#             j = 2
#             result = i * j
#             while result <= n:
#                 marker_array[result] = False
#                 j += 1
#                 result = i * j

#     primes = set()

#     for i in range(2, n + 1):
#         if marker_array[i] == True:
#             primes.add(i)
    
#     return primes

def check_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
# primes =  sieve_primes(n)

for i in range(1, n + 1): # considering 1 also as a prime number here, else change to n from n + 1
    if n % i == 0:
        res = n // i # no remainder as it divides exactly
        # if res in primes:
        if check_prime(res):
            print(res)
            break
