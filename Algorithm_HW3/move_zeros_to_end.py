def move_zeros(arr):
    j=0

    for num in arr:
        if num!= 0:
            arr[j] = num
            j=j+1
    while j < len(arr):
        arr[j] = 0
        j=j+1

    return arr

test_list = [0,7,0,5,0,0,4,3,2,4]
print(move_zeros(test_list))