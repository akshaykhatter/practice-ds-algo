def printPowerSet(test_string: str):
    length = len(test_string)
    for i in range(2**length):
        bin_pattern = f'{i:0>{length}b}'
        str_pattern = ''
        for j in range(len(bin_pattern)):
            if bin_pattern[j] == '1':
                str_pattern = str_pattern + test_string[j]
        # print(str_pattern)
        printPermutationsWithAll(list(str_pattern), True)

# Memoization dictionary
permutationsDict = {}

def printPermutationsWithAll(test_string: list, willPrint: bool):
    all_strings = []

    if len(test_string) == 0:
        pass
    elif len(test_string) == 1:
        all_strings = test_string
    else:
        # Memoization
        key = tuple(sorted(test_string))
        value = permutationsDict.get(key, None)

        if value is not None:
            all_strings = value
            # print('memoization used')
            # print(permutationsDict)
        else:
            for char in test_string:
                test_string_without_char = test_string[:]
                test_string_without_char.remove(char)
                
                for i in printPermutationsWithAll(test_string_without_char, False):
                    all_strings.append(f'{char}{i}')

            permutationsDict[key] = all_strings

    if willPrint:
        print(all_strings)
    else:
        return all_strings

# printPermutationsWithAll(list('abcd'), True)
print(printPowerSet('abcd'))