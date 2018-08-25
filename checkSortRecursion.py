# DC - Divide and Conquer
# SC - Subtract and Conquer

def checkDC(test_list: list, startIndex: int, endIndex: int):
    length = endIndex - startIndex + 1
    if length < 2:
        return True
    elif length == 2:
        return test_list[startIndex] < test_list[startIndex+ 1]
    else:
        if length % 2 == 0:
            mid = length // 2
        else:
            mid = (length - 1) // 2
        
        return checkDC(test_list, startIndex, mid) and checkDC(test_list, mid + 1, endIndex)

def checkSC(test_list: list, startIndex: int, endIndex: int):
    length = endIndex - startIndex + 1
    if length < 2:
        return True
    else:
        return (test_list[endIndex -1] < test_list[endIndex]) and checkSC(test_list, startIndex, endIndex -1)


test_list = [1, 2, 3, 5, 10, 9]
# print(checkSC(test_list, 0, len(test_list) - 1))
print(checkDC(test_list, 0, len(test_list) - 1))