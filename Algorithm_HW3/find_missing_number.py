def list(arr_1, arr_2):
    list_2.sort()
    print(arr_1)
    print(arr_2)

    for num1,num2 in zip(arr_1, arr_2): # its zips the similar items together
        if num1 != num2:
            return num1

list_1 = [1,2,3,4,5,6,7]
list_2 = [3,7,2,1,4,6]
print(list(list_1,list_2))