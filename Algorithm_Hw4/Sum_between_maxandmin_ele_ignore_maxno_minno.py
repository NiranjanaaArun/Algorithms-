def max_min_number(arr):
    min_item = max_item = arr[0]
    min_index = max_index = i = 0

    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])

test_list = [4,87,52,2,9,8,89,65,6] # 8+9=17
result = max_min_number(test_list)
print(result)

