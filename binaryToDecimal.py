def binaryToDecimal(binary_str: str):
    length = len(binary_str)
    decimal = 0
    weight = 0
    for i in range(1, length + 1):
        decimal  = decimal + int(binary_str[-i]) * 2**weight
        weight = weight + 1
    
    return decimal

print(binaryToDecimal('10011'))