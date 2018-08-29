no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    aayush_max_sum, harshit_max_sum = list(map(int, str(input()).strip().split(' ')))
    aayush_sum = harshit_sum = 0
    aayush_cur = harshit_cur = 0

    while True:
        aayush_cur = harshit_cur + 1
        if (aayush_cur + aayush_sum) > aayush_max_sum:
            print('Harshit')
            break
        else:
            aayush_sum = aayush_sum + aayush_cur
        
        harshit_cur = aayush_cur + 1
        if (harshit_cur + harshit_sum) > harshit_max_sum:
            print('Aayush')
            break
        else:
            harshit_sum = harshit_sum + harshit_cur
