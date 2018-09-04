# this is used in https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b/

import math

# navive approach theta(n)
def count_set_bits_simple(num: int) -> int:
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

# brian kernigan's algorithm O(n)
def count_set_bits_brian(num: int) -> int:
    count = 0
    while num:
        count += 1
        num = num & (num - 1)
    return count

# this one does in O(1) using a lookup table
def count_set_bits_lookup(num: int) -> int:
    # indexes       0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15
    lookup_table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    count = 0

    while num:
        count += lookup_table[num & 0xF]
        num >>= 4
    return count


def get_total_no_of_bits(num: int) -> int:
    if math.ceil(math.log2(num)) == math.log2(num):
        return math.ceil(math.log2(num)) + 1
    else:
        return math.ceil(math.log2(num))

print(count_set_bits_lookup(254))