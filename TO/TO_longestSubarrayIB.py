# https://www.interviewbit.com/problems/longest-subarray-difference/#

def longestSubarray(A: list, B: int):
    length = len(A)
    for size in range(length, 1, -1):
        start_index_end = length - size
        for start_index in range(start_index_end + 1):
            temp = A[start_index: start_index + size]
            temp.sort()
            if (B > (temp[-1] - temp[0])) == True:
                return size
    return 0

print(longestSubarray([1,2,4], 2))