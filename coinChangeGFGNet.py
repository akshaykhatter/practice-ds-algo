# https://practice.geeksforgeeks.org/problems/coin-change/0/?ref=self

# coins_count = []
# coins_limit = []

# # see countUptoUtil.py
# def increment(index=-1):
#     global coins_count
#     if (index * -1) > len(coins_count):
#         return False
    
#     if coins_count[index] + 1 == coins_limit[index]:
#         coins_count[index] = 0
#         return increment(index - 1)
#     else:
#         coins_count[index] += 1
#         return True


# no_of_test_cases = int(input())


# for _ in range(no_of_test_cases):
#     m = int(input()) # not used
#     coins = list(map(int, str(input()).strip().split(' ')))
#     cents = int(input())

#     count = 0
#     for i in coins:
#         coins_limit.append((cents // i) + 1)
#         coins_count.append(0)
    
#     while True:
#         flag = increment() # increments coins_count
        
#         sum_coins = 0
#         for j in range(len(coins)):
#             sum_coins += coins[j] * coins_count[j]
#         if sum_coins == cents:
#             count += 1

#         if flag == False:
#             break

#     print(count)

def count(S, m, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if n > 0 and m <= 0:
        return 0

    return count(S, m - 1, n) + count(S, m, n - S[m - 1])

# print(count([1, 2, 3], 3, 4))
print(count([2, 5, 3, 6], 4, 10))

