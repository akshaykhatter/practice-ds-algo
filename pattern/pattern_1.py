n = int(input())

# u -> upper half, l -> lower half of pattern

u_s = 1
l_s = n * n - n + 1

upper_row_count = n // 2
lower_row_count = n - upper_row_count

for i in range(upper_row_count):
    for j in range(n):
        print(u_s, end='')
        u_s = u_s + 1
        if j != (n - 1):
            print('*', end='')
    print('')
    u_s = u_s + n

for i in range(lower_row_count):
    for j in range(n):
        print(l_s, end='')
        l_s = l_s + 1
        if j != (n - 1):
            print('*', end='')
    print('')
    next_i_effective_index = (n // 2) + (i + 1)
    corresponding_row_in_u_index = n - next_i_effective_index - 1
    corresponding_row_start_num = corresponding_row_in_u_index * 2 * n + 1
    corresponding_row_end_num = corresponding_row_start_num + (n - 1)
    l_s = corresponding_row_end_num + 1

# for n == 5
# 1 * 2 * 3 * 4 * 5
# 11 * 12 * 13 * 14 * 15
# 21 * 22 * 23 * 24 * 25
# 16 * 17 * 18 * 19 * 20
# 6 * 7 * 8 * 9 * 10

# for n == 4
# 1 * 2 * 3 * 4
# 9 * 10 * 11 * 12
# 13 * 14 * 15 * 16
# 5 * 6 * 7 * 8