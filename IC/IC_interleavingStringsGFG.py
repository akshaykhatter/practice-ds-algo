# https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/
# Implement dynamic programming

str_a = input('Enter string A: ')
str_b = input('Enter string B: ')
str_c = input('Enter string C: ')

counter_a = 0
counter_b = 0
counter_c = 0

def is_interleaving(counter_a, counter_b, counter_c):
    print(f'Called for a:{counter_a}, b:{counter_b}, c:{counter_c}')

    if len(str_c) != (len(str_a) + len(str_b)):
        return False
    
    if counter_a == len(str_a) and counter_b == len(str_b):
        return True
    
    if counter_a == len(str_a):
        if str_c[counter_c] == str_b[counter_b]:
            return is_interleaving(counter_a, counter_b + 1, counter_c + 1)
        else:
            return False
    
    if counter_b == len(str_b):
        if str_c[counter_c] == str_a[counter_a]:
            return is_interleaving(counter_a + 1, counter_b, counter_c + 1)
        else:
            return False
    
    if str_a[counter_a] == str_b[counter_b]:
         # recursive case
        return is_interleaving(counter_a + 1, counter_b, counter_c + 1) or is_interleaving(counter_a, counter_b + 1, counter_c + 1)
    else:
        if str_c[counter_c] == str_a[counter_a]:
            return is_interleaving(counter_a + 1, counter_b, counter_c + 1)
        elif str_c[counter_c] == str_b[counter_b]:
            return is_interleaving(counter_a, counter_b + 1, counter_c + 1)
        else:
            return False

print(is_interleaving(counter_a, counter_b, counter_c))