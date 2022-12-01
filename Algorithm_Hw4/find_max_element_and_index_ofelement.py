def max_element(arr):
    max_index=0
    max_element=arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_index = i
            max_element= arr[i]

    return[max_index, max_element]

test_list = [3,5,78,96,2,45,76]
print(max_element(test_list))

