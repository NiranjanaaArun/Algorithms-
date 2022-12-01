def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

test_number_1 = [1,2,5]
test_number_2 = [1,3,0]
test_number_3 = [9,9,9]

print(plus_one(test_number_1))
print(plus_one(test_number_2))
print(plus_one(test_number_3))
