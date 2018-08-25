def printPowerSet(test_string: str):
    length = len(test_string)
    for i in range(2**length):
        bin_pattern = f'{i:0>{length}b}'
        str_pattern = ''
        for j in range(len(bin_pattern)):
            if bin_pattern[j] == '1':
                str_pattern = str_pattern + test_string[j]
        print(str_pattern)


printPowerSet('hello')