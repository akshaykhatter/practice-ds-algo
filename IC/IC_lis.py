# Longest increasing subsequence
memoization_dict = {}

def lis(array: tuple, prev=-1):
    if len(array) == 0:
        return 0
    elif memoization_dict.get((array, prev), None) is not None:
        result =  memoization_dict[(array, prev)]
    else:
        if array[0] > prev:
            val1 = lis(array[1:], array[0]) + 1
            val2 = lis(array[1:], prev)
            result = max(val1, val2)
        else:
            result = lis(array[1:], prev)
        
    memoization_dict[(array, prev)] = result
    return result

array = tuple(map(int, str(input('Enter space seprated array of numbers: ')).rstrip().split()))
print(f'Largest increasing subseqence length is {lis(array)[0]}')
print(memoization_dict)
