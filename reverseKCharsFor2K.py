# Aakash asked this question on WhatsApp group

def reverseChars(string: str, k: int):
    string_list = list(string)
    quotient = len(string) // (2 * k)
    remainder = len(string) % (2 * k)
    
    for i in range(quotient):
        start = 2 * k * i
        end = start + k - 1
        for j in range(k // 2):
            string_list[start + j], string_list[end - j] = string_list[end - j], string_list[start + j]
    
    start = 2 * k * quotient
    end = start + min(remainder, k) - 1
    for j in range((end - start + 1) // 2):
        string_list[start + j], string_list[end - j] = string_list[end - j], string_list[start + j]
    
    return str(string_list)


a = 'abcdefghe'
print(reverseChars(a, 2))