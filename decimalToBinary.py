def decimalToBinary(num: int):
    binary = ''
    while num:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

decimal = int(input('Enter a decimal no: '))
print(f"{decimal}'s binary representation is {decimalToBinary(decimal)}")
