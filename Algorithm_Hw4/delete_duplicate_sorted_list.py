#takes input as a sorted list
#updates to remve duplicates
#remaining elements shifted to the left to fill emptied spaces
#fill remianing indices with 0
#return number of valid elements.
#No sets are allowed.

def delete_duplicates(arr):
    write_index = 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    print(arr)
    return write_index

test_list = [2,3,3,3,5,6,7,7,8,8,10,11]
result = delete_duplicates(test_list)
print(result)
