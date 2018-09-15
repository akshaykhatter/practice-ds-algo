total_sum, no_of_digits = list(map(int, str(input()).strip().split(' ')))

def print_combinations(total_sum, no_of_digits, answer = []):
    if total_sum == 0 and no_of_digits == 0:
        print(answer)
    elif total_sum != 0 and no_of_digits != 0:
        for i in range(0, 10):
            new_answer = answer[:]
            new_answer.append(i)
            print_combinations(total_sum - i, no_of_digits - 1, new_answer)


print_combinations(total_sum, no_of_digits)