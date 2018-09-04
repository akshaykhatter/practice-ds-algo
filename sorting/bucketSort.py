import math

def bucket_sort_0_and_1(arr: list):
    # create a list of (n = 10) buckets
    bucket_list = []
    for _ in range(10):
        bucket_list.append([])

    # insert every element into its correct bucket
    for i in arr:
        bucket_index = int(i * 10)
        bucket_list[bucket_index].append(i)
    
    # print(bucket_list)

    result = []

    # sort indiviual buckets and add to result list
    for b in bucket_list:
        if len(b) > 1:
            # using insertion sort
            for i in range(1, len(b)):
                curr_element = b[i]
                j = i
                while (j - 1) >= 0 and b[j - 1] > curr_element:
                    b[j] = b[j - 1]
                    j = j - 1
                b[j] = curr_element
        result.extend(b)
    
    return result


def bucket_sort(arr: list):
    no_of_buckets = 10
    
    # create a list of (n = 10) buckets
    bucket_list = []
    for _ in range(no_of_buckets):
        bucket_list.append([])

    # find max and min element
    max_element = min_element = arr[0]
    for i in arr:
        if i > max_element:
            max_element = i
        elif i < min_element:
            min_element = i
    
    divider = math.ceil((max_element + 1) / no_of_buckets)

    # insert every element into its correct bucket
    for i in arr:
        bucket_index = math.floor(i / divider)
        bucket_list[bucket_index].append(i)
    
    # print(bucket_list)

    result = []

    # sort indiviual buckets and add to result list
    for b in bucket_list:
        if len(b) > 1:
            # using insertion sort
            for i in range(1, len(b)):
                curr_element = b[i]
                j = i
                while (j - 1) >= 0 and b[j - 1] > curr_element:
                    b[j] = b[j - 1]
                    j = j - 1
                b[j] = curr_element
        result.extend(b)
    
    return result


print(bucket_sort_0_and_1([0.1, 0.43, 0.71, 0.45, 0.41]))
print(bucket_sort([22, 45, 12, 8, 10, 6, 72, 81, 33, 18, 50, 14]))