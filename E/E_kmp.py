def prepare_lps(pattern: list):
    lps_arr = []
    lps_arr.append(0)
    
    i = j = 0
    
    while i < len(pattern) and j < len(pattern):
        if pattern[i] == pattern[j]:
            lps_arr.append(lps_arr[j] + 1)
            i += 1
            j += 1
        else:
            lps_arr.append(0)
            j += 1
    
    print(lps_arr)
    
prepare_lps(list('ananab#banana'))