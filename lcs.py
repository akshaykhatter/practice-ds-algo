# Longest common subsequence

memoizationDict = {}

def lcs(str1: str, str2: str) -> tuple:

    # solution exists in memoization dictionary
    
    result = memoizationDict.get((str1, str2), None)
    if result is not None:
        print('solution already existed')
        return result

    # solution doesn't exist in memoization dictionary

    if len(str1) == 0 or len(str2) == 0:
        return ('',0)
    
    elif str1[-1] == str2[-1]:
        sequence, length = lcs(str1[:-1], str2[:-1])
        sequence = sequence + str1[-1]
        length = length + 1

        # update dict
        memoizationDict[(str1, str2)] = (sequence, length)        
        return (sequence, length)
    else:
        seq1, len1 = lcs(str1, str2[:-1])
        seq2, len2 = lcs(str1[:-1], str2)
        
        if len1 >= len2:
            # update dict
            memoizationDict[(str1, str2)] = (seq1, len1)  
            return (seq1, len1)
        else:
            # update dict
            memoizationDict[(str1, str2)] = (seq2, len2)        
            return (seq2, len2)
        
str1 = input('Enter 1st string: ')
str2 = input('Enter 2nd string: ')

sequence, length = lcs(str1, str2)
print(f"Sequence is {''.join(sequence)} and length is {length}")